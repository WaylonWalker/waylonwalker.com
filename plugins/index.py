from markata.hookspec import hook_impl
from pathlib import Path
from string import Template
import textwrap


@hook_impl
def save(markata):
    for page, page_conf in markata.config["archive"]["pages"].items():
        create_page(markata, page, **page_conf)


def create_page(
    markata,
    page,
    tags=None,
    status="published",
    template=None,
    card_template=None,
    filters=None,
):
    all_posts = reversed(sorted(markata.articles, key=lambda x: x["date"]))

    if type(tags) == str:
        tags = [tags]

    posts = [post for post in all_posts if post["status"] == status]

    description = markata.description

    if tags is not None:
        posts = [post for post in posts if set(post["tags"]) & set(tags)]
        description = f"{description} of {tags[0]}"

    if filters is not None:
        all_posts = reversed(sorted(markata.articles, key=lambda x: x["date"]))
        for filter, value in filters.items():
            posts = [post for post in all_posts if post[filter] == value]

    if template is None:
        template = markata.config["archive"]["archive_template"]

    cards = [create_card(post, card_template) for post in posts]

    with open(template) as f:
        template = Template(f.read())
    output_file = Path(markata.config["output_dir"]) / page / "index.html"
    canonical_url = f"{markata.config['url']}/{page}/"
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


def create_card(post, template=None):
    if template is None:
        return textwrap.dedent(
            f"""
            <li class='post'>
            <a href="/{post['slug']}/">
                <h2 class='title'>{post['title']}</h2>
                <p class='description'>{post['long_description']}</p>
                <p class='date'>{post['date'].year}-{post['date'].month}-{post['date'].day}</p>
            </a>
            </li>
            """
        )
    with open(template) as f:
        template = Template(f.read())
    post["article_html"] = post.article_html

    return template.safe_substitute(**post.to_dict())
