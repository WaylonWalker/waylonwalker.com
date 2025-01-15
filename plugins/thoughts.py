from markata.hookspec import hook_impl
import re
import requests
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from markata import Markata


def clean_title(title: str) -> str:
    # Remove parenthetical content that starts with a number
    title = re.sub(r"\(\d+[^)]*\)", "", title)
    # Trim whitespace
    title = title.strip()
    # Limit to 65 characters
    if len(title) > 65:
        title = title[:62] + "..."
    return title


def clean_description(text: str) -> str:
    # Remove markdown links
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Remove markdown formatting characters
    text = re.sub(r"[*_`#]", "", text)
    # Clean up any extra whitespace
    text = " ".join(text.split())
    return text


@hook_impl(trylast=True)
def load(markata: "Markata") -> None:
    posts = requests.get(
        "https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999"
    ).json()

    text_opacity_80 = "{.text-opacity-80}"
    for post in posts:
        cleaned_title = clean_title(post["title"])
        post["title"] = "💭 " + cleaned_title.lstrip("💭 ")
        post["path"] = f"thoughts-{post['id']}"
        post["slug"] = f"thoughts-{post['id']}"
        post["templateKey"] = "thoughts"
        post["markata"] = markata
        post["description"] = clean_description(post["message"][:120])
        post["content"] = f"""
!!! note
     This post is a [thought](https://thoughts.waylonwalker.com).  It's a short note that I make about someone else's
     content online.  Learn more about the process [[ thoughts ]]

Here's my thought on [{post["title"]}]({post["link"]})

---

{post["message"]}

---

{text_opacity_80}
This post was a thought by [Waylon Walker](https://waylonwalker.com) see all my
thoughts at
[https://waylonwalker.com/thoughts](https://waylonwalker.com/thoughts)
        """
        post["jinja"] = False
        post["published"] = True
        post["tags"] = post["tags"].split(",")

    thoughts = markata.Posts.parse_obj(
        {"posts": posts},
    )
    markata.posts.extend(thoughts.posts)
