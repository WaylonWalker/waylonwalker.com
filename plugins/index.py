from typing import Union, List
from markata.hookspec import hook_impl
from string import Template
from pathlib import Path


@hook_impl
def save(markata):
    for page, page_conf in markata.config["archive"]["pages"].items():
        create_page(markata, page, **page_conf)


def create_page(markata, page, tags=None, status="published"):
    all_posts = reversed(sorted(markata.articles, key=lambda x: x["date"]))

    if type(tags) == str:
        tags = [tags]

    posts = [post for post in all_posts if post["status"] == status]

    description = markata.description

    if tags is not None:
        posts = [post for post in posts if set(post["tags"]) & set(tags)]
        description = f"{description} of {tags[0]}"

    cards = [create_card(markata, post) for post in posts]
    with open(markata.config["archive"]["archive_template"]) as f:
        template = Template(f.read())
    if page == "archive":
        output_file = Path(markata.config["output_dir"]) / "archive" / "index.html"
        canonical_url = f"{markata.config['url']}/archive/"
    else:
        output_file = (
            Path(markata.config["output_dir"]) / "archive" / page / "index.html"
        )
        canonical_url = f"{markata.config['url']}/archive/{page}/"
    output_file.parent.mkdir(exist_ok=True, parents=True)

    with open(output_file, "w+") as f:
        f.write(
            template.safe_substitute(
                body="".join(cards),
                url=markata.config["url"],
                description=description,
                title=markata.config["title"],
                canonical_url=canonical_url,
            )
        )


def create_card(markata, post):
    return f"""
<li class='post'>
  <a href="/{post['slug']}/">
    <h2 class='title'>{post['title']}</h2>
    <p class='description'>{post['long_description']}</p>
    <p class='date'>{post['date'].year}-{post['date'].month}-{post['date'].day}</p>
  </a>
</li>
"""
