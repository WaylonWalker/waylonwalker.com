"""
Webmentions for Markata (webmention.io + Bridgy)

Adds a "Webmentions" section to each post by querying webmention.io’s API.
Works great with Bridgy: point your site's <link rel="webmention"> to
webmention.io and let Bridgy send mentions there; this plugin renders them.

# Installation

- `pip install requests`
- Add the plugin to your `markata.toml`

``` toml
hooks = [
  "markata.plugins.webmentions",
]
```

# Configuration

``` toml
[webmentions]
# Your canonical site, used to build absolute URLs for posts if they don't
# already define `canonical_url`.
site_url = "https://waylonwalker.com"

# Your domain registered at webmention.io (usually same as site_url host).
domain = "waylonwalker.com"

# Optional API token from https://webmention.io/settings (recommended—gives
# private+higher limits and lets you use domain-wide queries).
# You may supply it directly or with an env indirection like "env:WEBMENTION_IO_TOKEN".
token = "env:WEBMENTION_IO_TOKEN"

# How far back to fetch on a cold start (days).
lookback_days = 365

# Where to cache fetched mentions between builds.
cache_file = ".markata/webmentions.json"

# Maximum number of mentions to render per post (0 = unlimited).
max_per_post = 50

# When true, also render likes/reposts; when false, only replies/mentions.
include_reactions = true

# Optional: add a small header and minimal CSS (good defaults).
inject_css = true
section_heading = "Webmentions"
```

# Usage

1) Ensure your site advertises a webmention endpoint that points to webmention.io:
   <link rel="webmention" href="https://webmention.io/yourdomain.com/webmention">
   <link rel="pingback" href="https://webmention.io/yourdomain.com/xmlrpc">
   Bridgy will discover this and deliver mentions there.

2) Build your site with Markata. This plugin will:
   - Fetch or incrementally update a local cache of your mentions.
   - Match mentions whose `wm-target` equals each post’s canonical URL.
   - Append a rendered Webmentions section to each post’s HTML.

# Notes

- The plugin prefers `post.canonical_url`. If not set, it builds one from
  `[webmentions].site_url` + `post.url` (or path-derived slug).
- Webmention.io API used:
  - By domain: https://webmention.io/api/mentions.jf2?domain=...&token=...&since=...
  - By target: https://webmention.io/api/mentions.jf2?target=...
- The cache file is safe to delete; it will be recreated.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import pydantic
import requests
from markata.hookspec import hook_impl, register_attr


# --- helpers to locate config no matter where user places it ---
def _locate_cfg_namespace(markata) -> Optional[pydantic.BaseModel]:
    """
    Try several common locations/names:
    - top-level: [webmentions], [webmention], [bridgy]
    - nested under [markata.*]: [markata.webmentions], etc.
    Falls back to scanning model_dump keys.
    """
    candidates = (
        "webmentions",
        "webmention",
        "bridgy",
        "webmention_io",
        "webmentionio",
    )
    # direct top-level
    for key in candidates:
        obj = getattr(markata.config, key, None)
        if obj is not None:
            return obj
    # nested under markata
    root = getattr(markata.config, "markata", None)
    if root is not None:
        for key in candidates:
            obj = getattr(root, key, None)
            if obj is not None:
                return obj
    # last resort: dict scan
    try:
        data = markata.config.model_dump()
        for key in (
            "webmentions",
            "webmention",
            "bridgy",
            "webmention_io",
            "webmentionio",
        ):
            if key in data and isinstance(data[key], dict):
                # build a temporary pydantic model for type parity
                class _Tmp(pydantic.BaseModel):
                    model_config = pydantic.ConfigDict(extra="allow")

                return _Tmp(**data[key])
        if "markata" in data and isinstance(data["markata"], dict):
            for key in candidates:
                if key in data["markata"] and isinstance(data["markata"][key], dict):

                    class _Tmp2(pydantic.BaseModel):
                        model_config = pydantic.ConfigDict(extra="allow")

                    return _Tmp2(**data["markata"][key])
    except Exception:
        pass
    return None


MARKATA_PLUGIN_NAME = "Webmentions"
MARKATA_PLUGIN_PACKAGE_NAME = "webmentions"


def _expand_env(value: Optional[str]) -> Optional[str]:
    """Support 'env:VAR' values in config."""
    if not value or not isinstance(value, str):
        return value
    if value.startswith("env:"):
        return os.getenv(value.split(":", 1)[1], "")
    return value


class WebmentionsConfig(pydantic.BaseModel):
    site_url: str
    domain: str
    token: Optional[str] = None
    lookback_days: int = 365
    cache_file: Path = Path(".markata/webmentions.json")
    max_per_post: int = 50
    include_reactions: bool = True
    inject_css: bool = True
    section_heading: str = "Webmentions"

    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="allow",
        str_strip_whitespace=True,
        validate_default=True,
        populate_by_name=True,
    )


class Config(pydantic.BaseModel):
    # Optional so sites without webmentions config don't fail validation
    webmentions: Optional[WebmentionsConfig] = None


@hook_impl
@register_attr("config_models")
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


@dataclass
class WMStore:
    by_target: Dict[str, List[Dict[str, Any]]]
    last_sync_ts: float


def _load_cache(path: Path) -> WMStore:
    if not path.exists():
        return WMStore(by_target={}, last_sync_ts=0.0)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return WMStore(
            by_target=data.get("by_target", {}),
            last_sync_ts=float(data.get("last_sync_ts", 0.0)),
        )
    except Exception:
        return WMStore(by_target={}, last_sync_ts=0.0)


def _save_cache(path: Path, store: WMStore) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = {
        "by_target": store.by_target,
        "last_sync_ts": store.last_sync_ts,
    }
    path.write_text(json.dumps(tmp, ensure_ascii=False, indent=2), encoding="utf-8")


def _jf2_fetch(params: Dict[str, str]) -> Iterable[Dict[str, Any]]:
    """Yield items from webmention.io JF2 feed, following pagination if present."""
    url = "https://webmention.io/api/mentions.jf2"
    session = requests.Session()
    while True:
        r = session.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        items = data.get("children", []) or data.get("items", [])
        for it in items:
            yield it
        # simple pagination support
        next_url = data.get("next")
        if not next_url:
            break
        # If next is a full URL, reset params; otherwise, continue
        url = next_url
        params = {}


def _ts(dt_str: str) -> float:
    try:
        return datetime.fromisoformat(dt_str.replace("Z", "+00:00")).timestamp()
    except Exception:
        return 0.0


def _classify(wm: Dict[str, Any]) -> str:
    """Return one of: reply, mention, like, repost, rsvp, other."""
    prop = wm.get("wm-property") or wm.get("wm_property") or ""
    if prop in ("in-reply-to", "reply"):
        return "reply"
    if prop in ("mention-of", "mention"):
        return "mention"
    if prop in ("like-of", "like"):
        return "like"
    if prop in ("repost-of", "repost"):
        return "repost"
    if prop == "rsvp":
        return "rsvp"
    return "other"


def _avatar(wm: Dict[str, Any]) -> str:
    return (
        (wm.get("author") or {}).get("photo")
        or (wm.get("author") or {}).get("avatar")
        or ""
    )


def _author_name(wm: Dict[str, Any]) -> str:
    a = wm.get("author") or {}
    return a.get("name") or a.get("url") or "Someone"


def _cite_url(wm: Dict[str, Any]) -> str:
    return wm.get("url") or (wm.get("wm-source") or "")


def _content_text(wm: Dict[str, Any]) -> str:
    c = wm.get("content") or {}
    return (c.get("text") or "").strip()


def _target_url_for_post(markata, post, cfg: WebmentionsConfig) -> Optional[str]:
    # Prefer explicit canonical_url on the post
    if hasattr(post, "canonical_url") and post.canonical_url:
        return str(post.canonical_url).rstrip("/")
    # Next, try post.url (Markata often sets this)
    if hasattr(post, "url") and post.url:
        base = cfg.site_url.rstrip("/")
        return f"{base}/{str(post.url).lstrip('/')}".rstrip("/")
    # Fallback: derive from path slug (e.g., "my-post/" from post.path)
    if hasattr(post, "path"):
        slug = str(post.path).split(".", 1)[0]
        base = cfg.site_url.rstrip("/")
        return f"{base}/{slug.lstrip('/')}".rstrip("/")
    return None


def _render_section(
    heading: str, items: List[Dict[str, Any]], include_reactions: bool, limit: int
) -> str:
    # Partition
    replies_mentions: List[Dict[str, Any]] = []
    reactions: List[Dict[str, Any]] = []
    for it in items:
        kind = _classify(it)
        if kind in ("reply", "mention", "rsvp"):
            replies_mentions.append(it)
        else:
            reactions.append(it)

    def li_html(wm: Dict[str, Any]) -> str:
        kind = _classify(wm)
        name = _author_name(wm)
        url = _cite_url(wm)
        avatar = _avatar(wm)
        published = wm.get("published") or wm.get("wm-received")
        content = _content_text(wm)
        badge = {
            "reply": "💬",
            "mention": "🔗",
            "rsvp": "🎟️",
            "like": "❤️",
            "repost": "🔁",
            "other": "✨",
        }.get(kind, "✨")
        meta_bits = []
        if published:
            meta_bits.append(published[:10])
        meta = " • ".join(meta_bits) if meta_bits else ""
        img = (
            f'<img class="wm-avatar" src="{avatar}" alt="" loading="lazy">'
            if avatar
            else ""
        )
        text = (
            content
            or f"{name} {('liked' if kind == 'like' else 'mentioned your post')}"
        )
        return f"""
<li class="wm-item wm-{kind}">
  <a class="wm-author" href="{url}" rel="nofollow noopener">{img}<span class="wm-name">{name}</span></a>
  <span class="wm-badge" title="{kind}">{badge}</span>
  <div class="wm-text">{text}</div>
  <div class="wm-meta">{meta}</div>
</li>""".strip()

    def ul_block(title: str, subset: List[Dict[str, Any]]) -> str:
        if not subset:
            return ""
        if limit and limit > 0:
            subset = subset[:limit]
        lis = "\n".join(li_html(wm) for wm in subset)
        return f"""<h3 class="wm-subheading">{title}</h3>
<ul class="wm-list">
{lis}
</ul>"""

    reactions_block = ul_block("Reactions", reactions) if include_reactions else ""
    replies_block = ul_block("Replies & Mentions", replies_mentions)

    if not (replies_block or reactions_block):
        return ""

    return f"""
<section class="webmentions">
  <h2 class="wm-heading">{heading}</h2>
  {replies_block}
  {reactions_block}
</section>
""".strip()


def _css_block() -> str:
    return """
<style>
.webmentions{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--border,#2a2a2a)}
.wm-heading{font-size:1.25rem;margin:0 0 .5rem;font-weight:600}
.wm-subheading{font-size:1rem;margin:1rem 0 .25rem;font-weight:600;opacity:.8}
.wm-list{list-style:none;padding:0;margin:.25rem 0 0;display:grid;gap:.75rem}
.wm-item{display:grid;grid-template-columns:auto 1fr;grid-template-areas:"author badge" "text text" "meta meta";gap:.25rem .5rem;align-items:center}
.wm-author{grid-area:author;display:flex;gap:.5rem;align-items:center;text-decoration:none}
.wm-avatar{width:28px;height:28px;border-radius:9999px;object-fit:cover}
.wm-name{font-weight:600}
.wm-badge{grid-area:badge;justify-self:end;opacity:.8}
.wm-text{grid-area:text;opacity:.95}
.wm-meta{grid-area:meta;font-size:.85em;opacity:.6}
.wm-item.wm-like .wm-text{opacity:.8}
</style>
""".strip()


def _merge_by_target(store: WMStore, new_items: Iterable[Dict[str, Any]]) -> None:
    for it in new_items:
        target = (it.get("wm-target") or it.get("wm_target") or "").rstrip("/")
        if not target:
            continue
        bucket = store.by_target.setdefault(target, [])
        # de-dup by wm-id or url
        new_id = str(it.get("wm-id") or it.get("wm_id") or it.get("url") or id(it))
        if any(
            str(x.get("wm-id") or x.get("wm_id") or x.get("url")) == new_id
            for x in bucket
        ):
            continue
        bucket.append(it)
        # keep newest first
        bucket.sort(
            key=lambda x: _ts(x.get("published") or x.get("wm-received") or ""),
            reverse=True,
        )


def _fetch_incremental(cfg: WebmentionsConfig, store: WMStore) -> None:
    token = _expand_env(cfg.token)
    since_epoch = store.last_sync_ts
    if since_epoch <= 0:
        since_epoch = (
            datetime.now(timezone.utc) - timedelta(days=cfg.lookback_days)
        ).timestamp()
    since_str = datetime.fromtimestamp(since_epoch, tz=timezone.utc).isoformat()

    params = {"domain": cfg.domain, "per-page": "1000", "since": since_str}
    if token:
        params["token"] = token
    for item in _jf2_fetch(params):
        _merge_by_target(store, [item])

    store.last_sync_ts = time.time()


@hook_impl
def post_render(markata: "Markata") -> None:
    # If not configured, do nothing. Accept several common section names/paths.
    cfg_src = _locate_cfg_namespace(markata)
    if cfg_src is None:
        return
    # Load config and expand token if provided via env:
    cfg = WebmentionsConfig(
        **{
            **cfg_src.model_dump(),
            "token": _expand_env(getattr(cfg_src, "token", None)),
        }
    )

    cache = _load_cache(cfg.cache_file)

    # Incrementally refresh cache (domain-wide). Fast no-op if nothing new.
    try:
        _fetch_incremental(cfg, cache)
        _save_cache(cfg.cache_file, cache)
    except Exception as e:
        markata.console.print(
            f"[yellow]webmentions: fetch failed ({e}); using cache only[/yellow]"
        )

    used_css_once = False

    for post in markata.posts:
        # skip drafts/hidden if present
        if hasattr(post, "published") and not post.published:
            continue

        target = _target_url_for_post(markata, post, cfg)
        if not target:
            continue

        items = cache.by_target.get(target, [])
        if not items:
            continue

        html_block = _render_section(
            heading=cfg.section_heading,
            items=items,
            include_reactions=cfg.include_reactions,
            limit=cfg.max_per_post,
        )
        if not html_block:
            continue

        # Inject optional CSS only once per build (first time we actually render).
        css = _css_block() if (cfg.inject_css and not used_css_once) else ""
        used_css_once = used_css_once or bool(css)

        # Append to rendered content
        # Markata posts usually have `.content` (HTML) after render hooks.
        current = getattr(post, "content", None) or getattr(post, "html", "")
        combined = f"{current}\n{css}\n{html_block}"
        if hasattr(post, "content"):
            post.content = combined
        else:
            post.html = combined


# Optional: small CLI helper to force a refresh (e.g., `markata webmentions-refresh`)
@hook_impl()
def cli(app, markata):
    @app.command()
    def webmentions_refresh():
        """Force-refresh the domain-wide webmention cache."""
        cfg_src = _locate_cfg_namespace(markata)
        if cfg_src is None:
            print("webmentions is not configured in markata.toml; nothing to refresh.")
            return
        cfg = WebmentionsConfig(
            **{
                **cfg_src.model_dump(),
                "token": _expand_env(getattr(cfg_src, "token", None)),
            }
        )
        cache = _load_cache(cfg.cache_file)
        _fetch_incremental(cfg, cache)
        _save_cache(cfg.cache_file, cache)
        print(
            f"Updated {cfg.cache_file} with {sum(len(v) for v in cache.by_target.values())} mentions."
        )
