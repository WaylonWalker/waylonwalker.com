from typing import Union, List
from markata.hookspec import hook_impl
from string import Template
from pathlib import Path


@hook_impl
def save(markata):
    for page, page_conf in markata.config["archive"]["pages"].items():
        create_page(markata, page, **page_conf)


def create_page(markata, page, tags=None):
    all_posts = reversed(sorted(markata.articles, key=lambda x: x["date"]))

    if type(tags) == str:
        tags = [tags]

    posts = [post for post in all_posts if post["status"] == "published"]

    if tags is not None:
        posts = [post for post in posts if set(post["tags"]) & set(tags)]

    cards = [create_card(markata, post) for post in posts]
    with open(markata.config["archive"]["archive_template"]) as f:
        template = Template(f.read())
    if page == "archive":
        output_file = Path(markata.config["output_dir"]) / "archive" / "index.html"
    else:
        output_file = (
            Path(markata.config["output_dir"]) / "archive" / page / "index.html"
        )
    output_file.parent.mkdir(exist_ok=True, parents=True)
    with open(output_file, "w+") as f:
        print("writing index")
        f.write(
            template.safe_substitute(
                body="".join(cards),
                url=markata.config["url"],
                descriiption=markata.config["description"],
                title=markata.config["title"],
            )
        )


def create_card(markata, post):
    return f"""
<li class='post'>
  <a href="{"/" + post['slug']}">
    <h2 class='title'>{post['title']}</h2>
    <p class='description'>{post['long_description']}</p>
    <p class='date'>{post['date'].year}-{post['date'].month}-{post['date'].day}</p>
  </a>
</li>
"""
