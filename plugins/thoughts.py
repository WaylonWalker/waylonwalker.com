from typing import TYPE_CHECKING

import requests
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from markata import Markata


@hook_impl(trylast=True)
def load(markata: "Markata") -> None:
    posts = requests.get(
        "https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999"
    ).json()

    for post in posts:
        post["title"] = "💭 " + post["title"].lstrip("💭 ")
        post["path"] = f"thoughts-{post['id']}"
        post["slug"] = f"thoughts-{post['id']}"
        post["templateKey"] = "thoughts"
        post["markata"] = markata
        post["content"] = f"""
This post is a [thought](https://thoughts.waylonwalker.com).  It's a short note that I make about someone else's
content online.  Learn more about the process [here](https://waylonwalker.com/thoughts)

Here's my thought on [{post["title"]}]({post["link"]})

---

{post["message"]}

---

This post was a thought by [Waylon Walker](https://waylonwalker.com) see all my thoughts at [https://waylonwalker.com/thoughts](https://waylonwalker.com/thoughts)
        """
        post["jinja"] = False
        post["published"] = True

    thoughts = markata.Posts.parse_obj(
        {"posts": posts},
    )
    markata.posts.extend(thoughts.posts)
