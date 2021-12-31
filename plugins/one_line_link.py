import re
import textwrap

import background
import requests
import twitter
from bs4 import BeautifulSoup
from markata.hookspec import hook_impl

RE_ONE_LINE = re.compile("^https://waylonwalker.com/.*")
RE_TWEET = re.compile("^https://twitter.com/.*")

API = twitter.Api()


def expand_line(line):
    """
    Todo: better error message over base exception
    Todo: try except decorator?
    """
    try:
        r = RE_ONE_LINE.match(line)
        if r and " " not in line:
            return get_one_line_link(line)
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


def get_one_line_link(link):
    r = requests.get(link)
    if r.status_code != 200:
        return link
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        url = soup.find("meta", attrs={"name": "og:url"})["content"]
    except KeyError:
        url = link
    except TypeError:
        url = link

    try:
        sm_img = soup.find("meta", attrs={"name": "og:sm_image"})["content"]
    except KeyError:
        try:
            sm_img = soup.find("meta", attrs={"name": "og:image"})["content"]
        except KeyError:
            raise OneLineLinkError(f"could not find sm_img on {link}")
    except TypeError:
        try:
            sm_img = soup.find("meta", attrs={"name": "og:image"})["content"]
        except KeyError:
            raise OneLineLinkError(f"could not find sm_img on {link}")
        except TypeError:
            raise OneLineLinkError(f"could not find sm_img on {link}")

    try:
        title = soup.find("title").text
    except KeyError:
        try:
            title = soup.find("meta", attrs={"name": "og:title"})["content"]
        except KeyError:
            raise OneLineLinkError(f"could not find title on {link}")
        except TypeError:
            raise OneLineLinkError(f"could not find title on {link}")
    except TypeError:
        try:
            title = soup.find("meta", attrs={"name": "og:title"})["content"]
        except KeyError:
            raise OneLineLinkError(f"could not find title on {link}")
        except TypeError:
            raise OneLineLinkError(f"could not find title on {link}")

    try:
        description = soup.find("meta", attrs={"name": "og:description"})["content"]
    except KeyError:
        description = soup.text[:120]
    except TypeError:
        description = soup.text[:120]

    description = description.replace("\n", " ").replace("\r", "")

    return textwrap.dedent(
        f"""
    <div class="onelinelink-wrapper">
        <a class="onelinelink" href="{url}">
            <img style="float: right;" align='right' src="{sm_img}" alt="article cover for {title}"/>
            <div class="right">
                <h2>{title}</h2>
                <p class="description">
                {description}
                </p>
                <p class="url">
                <span class="read-more">read more</span>  waylonwalker.com
                </p>
            </div>
        </a>
    </div>
    """
    )


background.n = 100


def expand_article(content):
    return "\n".join([expand_line(line) for line in content.split("\n")])


@hook_impl
def pre_render(markata):
    with markata.cache as cache:
        for article in markata.articles:

            html_key = markata.make_hash(
                "one_line_link", "render", "html", article["content_hash"]
            )
            expanded_content_key = markata.make_hash(
                "one_line_link", "render", "expanded_content", article["content_hash"]
            )
            html_from_cache = cache.get(html_key)
            expanded_content_from_cache = cache.get(expanded_content_key)

            # html_from_cache = None
            # expanded_content_from_cache = None

            if expanded_content_from_cache is None:
                expanded_content = expand_article(article.content)
                cache.add(expanded_content_key, expanded_content)
            else:
                expanded_content = expanded_content_from_cache

            if html_from_cache is None:
                html = markata.md.convert(expanded_content)
                cache.add(html_key, html)
            else:
                html = html_from_cache

            article.content = expanded_content
            article.html = html
            article.article_html = html
