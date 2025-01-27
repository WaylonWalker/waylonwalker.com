import re
import textwrap

from markata.hookspec import hook_impl
import twitter

RE_ONE_LINE = re.compile("^https://waylonwalker.com/.*")
RE_TWEET = re.compile("^https://twitter.com/.*")

API = twitter.Api()


def expand_line(line, markata):
    """
    Todo: better error message over base exception
    Todo: try except decorator?
    """
    try:
        r = RE_ONE_LINE.match(line)
        if r and " " not in line:
            return get_one_line_link(line, markata=markata)
        r = RE_TWEET.match(line)
        if r and " " not in line:
            html = API.GetStatusOembed(url=line)["html"]
            return html

        return line
    except BaseException as e:
        import warnings

        warnings.warn(f"OneLineLink threw an error\n {e}")

        return line


class OneLineLinkError(KeyError):
    pass


def get_one_line_link(link, markata):
    slug = link.replace("https://waylonwalker.com/", "").strip("/")
    if slug not in markata.map("slug"):
        return link
    post = markata.map("post", f'slug=="{slug}"')[0]
    root_url = markata.get_config("url") or ""
    url = f'{root_url}/{post.metadata["slug"]}/'
    img = f"https://covers.waylonwalker.com/{slug}.jpg"
    title = post.get("title", "")
    description = post.get("description", "")

    return textwrap.dedent(
        f"""
    <div class="onelinelink-wrapper">
        <a class="onelinelink" href="{url}">
            <img style="float: right;" align='right' src="{img}" alt="article cover for {title}"/>
            <p><strong>{title}</strong></p>
        </a>
    </div>
    """
    )


def expand_article(content, markata):
    return "\n".join(
        [expand_line(line, markata=markata) for line in content.split("\n")]
    )


@hook_impl
def pre_render(markata):
    with markata.cache as cache:
        for article in markata.articles:
            expanded_content_key = markata.make_hash(
                "one_line_link", "render", "expanded_content", article.content
            )
            expanded_content_from_cache = cache.get(expanded_content_key)

            if expanded_content_from_cache is None:
                expanded_content = expand_article(article.content, markata=markata)
                cache.set(expanded_content_key, expanded_content)
            else:
                expanded_content = expanded_content_from_cache

            article.content = expanded_content
