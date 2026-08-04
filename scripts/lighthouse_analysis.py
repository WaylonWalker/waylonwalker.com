#!/usr/bin/env python3
"""Run Lighthouse across representative pages and generate comparison reports."""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin


CATEGORIES = ["performance", "accessibility", "best-practices", "seo"]
COMPACT_FINDING_IGNORES = {
    "bootup-time",
    "dom-size",
    "first-contentful-paint",
    "first-meaningful-paint",
    "interactive",
    "largest-contentful-paint",
    "largest-contentful-paint-element",
    "mainthread-work-breakdown",
    "max-potential-fid",
    "network-dependency-tree-insight",
    "render-blocking-insight",
    "render-blocking-resources",
    "server-response-time",
    "speed-index",
    "total-blocking-time",
}


@dataclass(frozen=True)
class Page:
    key: str
    label: str
    path: str


PAGES = [
    Page("home", "Home", "/"),
    Page("about-site", "About This Site", "/about-this-site/"),
    Page("article", "Article: Tmux Session Switcher", "/i-built-a-tmux-session-switcher/"),
    Page("feeds", "Feeds", "/feeds/"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Lighthouse on representative pages and generate HTML plus agent reports.",
    )
    parser.add_argument(
        "--base-url",
        default="https://waylonwalker.com",
        help="Base site URL used with the built-in page set.",
    )
    parser.add_argument(
        "--pages",
        default=",".join(page.key for page in PAGES),
        help="Comma-separated page keys to scan. Available: %s" % ", ".join(page.key for page in PAGES),
    )
    parser.add_argument(
        "--output-dir",
        default=".markata/lighthouse-analysis",
        help="Directory to store raw JSON, HTML, and compact agent reports.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=300,
        help="Per-page Lighthouse timeout in seconds.",
    )
    parser.add_argument(
        "--chrome-flags",
        default="--headless=new --no-sandbox",
        help="Chrome flags passed through to Lighthouse.",
    )
    return parser.parse_args()


def require_binary(name: str) -> None:
    if shutil.which(name):
        return
    raise SystemExit(f"missing required dependency: {name}")


def score_to_int(score: Any) -> int:
    if score is None:
        return 0
    return int(round(float(score) * 100))


def metric_value(audits: dict[str, Any], key: str) -> float | None:
    metric = audits.get(key, {})
    value = metric.get("numericValue")
    if value is None:
        return None
    return float(value)


def format_ms(value: float | None) -> str:
    if value is None:
        return "-"
    if value >= 1000:
        return f"{value / 1000:.2f}s"
    return f"{value:.0f}ms"


def format_seconds(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value / 1000:.2f}s"


def format_cls(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.3f}"


def run_lighthouse(url: str, json_path: Path, timeout_seconds: int, chrome_flags: str) -> None:
    cmd = [
        "lighthouse",
        url,
        "--quiet",
        f"--chrome-flags={chrome_flags}",
        "--only-categories=" + ",".join(CATEGORIES),
        "--output=json",
        f"--output-path={json_path}",
    ]
    subprocess.run(cmd, check=True, timeout=timeout_seconds, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def collect_failed_audits(report: dict[str, Any]) -> list[dict[str, str]]:
    audits = report["audits"]
    audit_ids: set[str] = set()
    for category_name in CATEGORIES:
        refs = report["categories"][category_name]["auditRefs"]
        audit_ids.update(ref["id"] for ref in refs)

    failed: list[dict[str, str]] = []
    for audit_id in sorted(audit_ids):
        audit = audits[audit_id]
        score = audit.get("score")
        if score is None or score >= 1:
            continue
        if audit.get("scoreDisplayMode") == "notApplicable":
            continue
        failed.append(
            {
                "id": audit_id,
                "title": audit.get("title", audit_id),
                "display_value": audit.get("displayValue", "") or "",
                "description": audit.get("description", "") or "",
            }
        )
    return failed


def parse_report(page: Page, url: str, report: dict[str, Any]) -> dict[str, Any]:
    category_scores = {
        name: score_to_int(report["categories"][name]["score"])
        for name in CATEGORIES
    }
    audits = report["audits"]
    return {
        "key": page.key,
        "label": page.label,
        "url": url,
        "scores": category_scores,
        "metrics": {
            "lcp_ms": metric_value(audits, "largest-contentful-paint"),
            "tbt_ms": metric_value(audits, "total-blocking-time"),
            "cls": metric_value(audits, "cumulative-layout-shift"),
            "si_ms": metric_value(audits, "speed-index"),
        },
        "failed_audits": collect_failed_audits(report),
    }


def average_scores(results: list[dict[str, Any]]) -> dict[str, int]:
    averages: dict[str, int] = {}
    for category in CATEGORIES:
        values = [page["scores"][category] for page in results]
        averages[category] = int(round(sum(values) / len(values))) if values else 0
    return averages


def previous_summary(output_dir: Path) -> dict[str, Any] | None:
    latest = output_dir / "latest" / "summary.json"
    if not latest.exists():
        return None
    return json.loads(latest.read_text())


def diff_map(current: dict[str, int], previous: dict[str, int] | None) -> dict[str, int | None]:
    if not previous:
        return {key: None for key in current}
    return {key: current[key] - previous.get(key, current[key]) for key in current}


def change_badge(delta: int | None) -> str:
    if delta is None:
        return "new"
    if delta == 0:
        return "0"
    sign = "+" if delta > 0 else ""
    return f"{sign}{delta}"


def compact_findings(page: dict[str, Any], limit: int = 3) -> list[str]:
    findings = []
    for audit in page["failed_audits"]:
        if audit["id"] in COMPACT_FINDING_IGNORES:
            continue
        line = audit["title"]
        if audit["display_value"]:
            line += f" ({audit['display_value']})"
        findings.append(line)
        if len(findings) >= limit:
            break
    return findings


def render_markdown(summary: dict[str, Any], previous: dict[str, Any] | None) -> str:
    avg_diff = diff_map(summary["averages"], previous["averages"] if previous else None)
    lines = [
        f"# Lighthouse Summary: {summary['base_url']}",
        "",
        f"Run: `{summary['run_id']}`",
        "",
        "## Averages",
        "",
        "| Category | Score | Delta |",
        "|---|---:|---:|",
    ]
    for category in CATEGORIES:
        lines.append(
            f"| {category} | {summary['averages'][category]} | {change_badge(avg_diff[category])} |"
        )

    lines.extend(["", "## Pages", ""])
    for page in summary["pages"]:
        prev_page = None
        if previous:
            prev_page = next((item for item in previous["pages"] if item["key"] == page["key"]), None)
        score_delta = diff_map(page["scores"], prev_page["scores"] if prev_page else None)
        lines.append(f"### {page['label']}")
        lines.append(f"- URL: {page['url']}")
        score_bits = ", ".join(
            f"{name} {page['scores'][name]} ({change_badge(score_delta[name])})"
            for name in CATEGORIES
        )
        lines.append(f"- Scores: {score_bits}")
        lines.append(
            "- Metrics: "
            + f"LCP {format_seconds(page['metrics']['lcp_ms'])}, "
            + f"TBT {format_ms(page['metrics']['tbt_ms'])}, "
            + f"CLS {format_cls(page['metrics']['cls'])}, "
            + f"Speed Index {format_seconds(page['metrics']['si_ms'])}"
        )
        findings = compact_findings(page)
        if findings:
            lines.append("- Top findings: " + "; ".join(findings))
        else:
            lines.append("- Top findings: none")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def render_text(summary: dict[str, Any], previous: dict[str, Any] | None) -> str:
    lines = [f"Lighthouse Summary :: {summary['base_url']}", f"Run :: {summary['run_id']}", ""]
    avg_diff = diff_map(summary["averages"], previous["averages"] if previous else None)
    lines.append(
        "Averages :: "
        + ", ".join(
            f"{name} {summary['averages'][name]} ({change_badge(avg_diff[name])})" for name in CATEGORIES
        )
    )
    lines.append("")
    for page in summary["pages"]:
        prev_page = None
        if previous:
            prev_page = next((item for item in previous["pages"] if item["key"] == page["key"]), None)
        score_delta = diff_map(page["scores"], prev_page["scores"] if prev_page else None)
        lines.append(page["label"])
        lines.append(page["url"])
        lines.append(
            "  Scores :: "
            + ", ".join(
                f"{name} {page['scores'][name]} ({change_badge(score_delta[name])})" for name in CATEGORIES
            )
        )
        lines.append(
            "  Metrics :: "
            + f"LCP {format_seconds(page['metrics']['lcp_ms'])}, "
            + f"TBT {format_ms(page['metrics']['tbt_ms'])}, "
            + f"CLS {format_cls(page['metrics']['cls'])}"
        )
        findings = compact_findings(page)
        lines.append("  Findings :: " + ("; ".join(findings) if findings else "none"))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def render_html(summary: dict[str, Any], previous: dict[str, Any] | None) -> str:
    avg_diff = diff_map(summary["averages"], previous["averages"] if previous else None)
    cards = []
    for category in CATEGORIES:
        cards.append(
            f"""
            <div class=\"score-card\">
              <div class=\"score-label\">{html.escape(category)}</div>
              <div class=\"score-value\">{summary['averages'][category]}</div>
              <div class=\"score-delta\">{html.escape(change_badge(avg_diff[category]))}</div>
            </div>
            """
        )

    page_rows = []
    for page in summary["pages"]:
        prev_page = None
        if previous:
            prev_page = next((item for item in previous["pages"] if item["key"] == page["key"]), None)
        score_delta = diff_map(page["scores"], prev_page["scores"] if prev_page else None)
        badges = "".join(
            f"<span class=\"mini-score\"><strong>{html.escape(name)}</strong> {page['scores'][name]} <em>{html.escape(change_badge(score_delta[name]))}</em></span>"
            for name in CATEGORIES
        )
        findings = compact_findings(page, limit=5)
        findings_html = "".join(f"<li>{html.escape(item)}</li>" for item in findings) or "<li>No notable failures.</li>"
        page_rows.append(
            f"""
            <section class=\"page-card\">
              <header>
                <h2>{html.escape(page['label'])}</h2>
                <a href=\"{html.escape(page['url'])}\">{html.escape(page['url'])}</a>
              </header>
              <div class=\"score-row\">{badges}</div>
              <div class=\"metric-grid\">
                <div><span>LCP</span><strong>{html.escape(format_seconds(page['metrics']['lcp_ms']))}</strong></div>
                <div><span>TBT</span><strong>{html.escape(format_ms(page['metrics']['tbt_ms']))}</strong></div>
                <div><span>CLS</span><strong>{html.escape(format_cls(page['metrics']['cls']))}</strong></div>
                <div><span>Speed Index</span><strong>{html.escape(format_seconds(page['metrics']['si_ms']))}</strong></div>
              </div>
              <div class=\"findings\">
                <h3>Top findings</h3>
                <ul>{findings_html}</ul>
              </div>
            </section>
            """
        )

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Lighthouse Analysis</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #0b1020;
      --panel: rgba(17, 24, 39, 0.9);
      --panel-2: rgba(30, 41, 59, 0.9);
      --border: rgba(148, 163, 184, 0.18);
      --text: #e5eefc;
      --muted: #94a3b8;
      --accent: #7dd3fc;
      --shadow: 0 24px 80px rgba(2, 6, 23, 0.45);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font: 16px/1.5 Inter, ui-sans-serif, system-ui, sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top, rgba(14, 165, 233, 0.18), transparent 35%),
        radial-gradient(circle at right, rgba(168, 85, 247, 0.16), transparent 30%),
        var(--bg);
    }}
    a {{ color: var(--accent); }}
    .wrap {{ max-width: 1180px; margin: 0 auto; padding: 40px 24px 64px; }}
    .hero, .page-card, .score-card {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 20px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(18px);
    }}
    .hero {{ padding: 28px; margin-bottom: 24px; }}
    .hero h1 {{ margin: 0 0 8px; font-size: 2rem; }}
    .hero p {{ margin: 0; color: var(--muted); }}
    .score-overview {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-bottom: 24px; }}
    .score-card {{ padding: 18px 20px; }}
    .score-label {{ text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); font-size: 0.78rem; }}
    .score-value {{ font-size: 2.2rem; font-weight: 700; margin: 6px 0; }}
    .score-delta {{ color: var(--accent); font-weight: 600; }}
    .page-list {{ display: grid; gap: 18px; }}
    .page-card {{ padding: 22px; }}
    .page-card header {{ display: flex; justify-content: space-between; gap: 16px; align-items: baseline; flex-wrap: wrap; }}
    .page-card h2 {{ margin: 0; font-size: 1.25rem; }}
    .score-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0 18px; }}
    .mini-score {{ padding: 8px 12px; border-radius: 999px; background: var(--panel-2); border: 1px solid var(--border); color: var(--text); }}
    .mini-score em {{ font-style: normal; color: var(--muted); margin-left: 6px; }}
    .metric-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; margin-bottom: 18px; }}
    .metric-grid div {{ padding: 14px; background: rgba(15, 23, 42, 0.78); border-radius: 14px; border: 1px solid var(--border); }}
    .metric-grid span {{ display: block; color: var(--muted); font-size: 0.82rem; margin-bottom: 6px; }}
    .metric-grid strong {{ font-size: 1.05rem; }}
    .findings h3 {{ margin: 0 0 10px; font-size: 0.95rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; }}
    .findings ul {{ margin: 0; padding-left: 20px; }}
    .footer-note {{ margin-top: 18px; color: var(--muted); font-size: 0.92rem; }}
  </style>
</head>
<body>
  <div class=\"wrap\">
    <section class=\"hero\">
      <h1>Lighthouse Analysis</h1>
      <p>Run <code>{html.escape(summary['run_id'])}</code> for <strong>{html.escape(summary['base_url'])}</strong>. Deltas compare against the previous saved run.</p>
    </section>
    <section class=\"score-overview\">{''.join(cards)}</section>
    <section class=\"page-list\">{''.join(page_rows)}</section>
    <p class=\"footer-note\">Raw Lighthouse JSON for each page is stored alongside this report so reruns can be compared later.</p>
  </div>
</body>
</html>
"""


def write_latest(output_dir: Path, run_dir: Path) -> None:
    latest_dir = output_dir / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    for name in ["summary.json", "agent.md", "agent.txt", "report.html"]:
        shutil.copy2(run_dir / name, latest_dir / name)


def main() -> int:
    args = parse_args()
    require_binary("lighthouse")

    selected = {item.strip() for item in args.pages.split(",") if item.strip()}
    pages = [page for page in PAGES if page.key in selected]
    if not pages:
        raise SystemExit("no valid pages selected")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    previous = previous_summary(output_dir)

    run_id = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    run_dir = output_dir / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    for page in pages:
        url = urljoin(args.base_url.rstrip("/") + "/", page.path.lstrip("/"))
        json_path = run_dir / f"{page.key}.json"
        print(f"analyzing {page.label}: {url}", file=sys.stderr)
        run_lighthouse(url, json_path, args.timeout_seconds, args.chrome_flags)
        report = json.loads(json_path.read_text())
        results.append(parse_report(page, url, report))

    summary = {
        "run_id": run_id,
        "generated_at": datetime.now(UTC).isoformat(),
        "base_url": args.base_url,
        "pages": results,
        "averages": average_scores(results),
    }

    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (run_dir / "agent.md").write_text(render_markdown(summary, previous))
    (run_dir / "agent.txt").write_text(render_text(summary, previous))
    (run_dir / "report.html").write_text(render_html(summary, previous))
    write_latest(output_dir, run_dir)

    print(f"HTML report: {run_dir / 'report.html'}")
    print(f"Agent report: {run_dir / 'agent.md'}")
    print(f"Text report: {run_dir / 'agent.txt'}")
    print(f"Latest snapshot: {output_dir / 'latest' / 'summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
