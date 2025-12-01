"""md_video plugin"""

from markata.hookspec import hook_impl
import pydantic
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from markata import Markata

MARKATA_PLUGIN_NAME = "md_video"
MARKATA_PLUGIN_PACKAGE_NAME = "md-video"


class MdVideoConfig(pydantic.BaseModel):
    video_extensions: list[str] = [".mp4", ".avi", ".webm"]
    output_format: str = "mp4"


class Config(pydantic.BaseModel):
    md_video: MdVideoConfig = MdVideoConfig()


@hook_impl
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


def convert_media_tags(markata: "Markata", post) -> str:
    """Convert Markdown image tags with video extensions to video tags."""
    image_pattern = re.compile(r"!\[(.*?)\]\((.*?)(\.\w+)\)")

    md_video_conversions = []

    def replace_image_with_video(match):
        alt_text, src, ext = match.groups()
        if ext.lower() in markata.config.md_video.video_extensions:
            md_video_conversions.append(
                f"* [[ {post.slug} ]] -> [{src}{ext}]({src}{ext})"
            )
            return f'<video autoplay loop muted playsinline controls><source src="{src}{ext}" type="video/{ext[1:]}">Your browser does not support the video tag.</video>'
        return match.group(0)

    return md_video_conversions, image_pattern.sub(
        replace_image_with_video, post.content
    )


@hook_impl
# @register_attr("md_video_conversions")
def pre_render(markata: "Markata") -> None:
    with markata.cache as cache:
        for post in markata.filter("not skip"):
            content_key = markata.make_hash("md_video_content", post.content)
            content = cache.get(content_key)
            # conversions_key = markata.make_hash("md_video_conversions", post.content)
            # conversions = cache.get(conversions_key)

            if content is None:
                md_video_conversions, post.content = convert_media_tags(markata, post)
                # markata.md_video_conversions.extend(md_video_conversions)
                cache.set(content_key, post.content)
                # cache.set(conversions_key, markata.md_video_conversions)
                continue
            else:
                post.content = content
                # markata.md_video_conversions.extend(conversions)

    # # Create a report post
    # content_lines = [
    #     "# md-video Report",
    #     "",
    #     "## Converted Videos",
    #     "",
    #     *markata.md_video_conversions,
    # ]
    #
    # content = "\n".join(content_lines)

    # post_args = {
    #     "markata": markata,
    #     "templateKey": "plugin-report",
    #     "path": f'{MARKATA_PLUGIN_PACKAGE_NAME.strip().replace("_", "-")}.md',
    #     "content": content,
    #     "raw": content,
    #     "tags": ["plugin-report"],
    #     "slug": f"{MARKATA_PLUGIN_PACKAGE_NAME.strip().replace('_', '-')}-plugin-report",
    #     "title": "md-video Report",
    #     "description": "Generated report from the md-video plugin",
    #     "published": False,
    #     "date": datetime.now().isoformat(),
    # }
    #
    # post = markata.Post.parse_obj(post_args)
    # markata.Post.validate(post)
    # markata.posts.append(post)
