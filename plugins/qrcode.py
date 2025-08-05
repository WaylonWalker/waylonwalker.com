"""
QRCode Plugin

Generates QR codes for selected posts and saves them to `markout/<slug>/qr.svg`.

# Installation

```toml
[tool.markata]
hooks = ["markata.plugins.qrcode"]
```

Install dependencies:

```bash
pip install pyqrcode
```

# Configuration

```toml
[markata.qrcode]
filter = "True"                  # Python expression to filter posts
module_color = "#000000"         # Color of the QR modules (foreground)
background = "#ffffff"           # Background color of the QR code
scale = 8                        # If scale <= 0, sets omithw=True
```

# Usage

This plugin runs during the `post_render` phase and generates a QR code SVG at:
`markout/<slug>/qr.svg` based on the post’s URL.

# Notes

- If `scale <= 0`, `omithw=True` will be used instead of scale.
- Ensure post URLs are correctly formed before this plugin runs.
"""

from markata.hookspec import hook_impl, register_attr
import pydantic
from pathlib import Path
import pyqrcode
from typing import Optional


MARKATA_PLUGIN_NAME = "QRCode"
MARKATA_PLUGIN_PACKAGE_NAME = "qrcode"


class QRCodeConfig(pydantic.BaseModel):
    filter: str = "True"
    module_color: Optional[str] = "#000000"
    background: Optional[str] = "#ffffff"
    scale: int = -1

    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="allow",
        str_strip_whitespace=True,
        validate_default=True,
        coerce_numbers_to_str=True,
        populate_by_name=True,
    )


class Config(pydantic.BaseModel):
    qrcode: QRCodeConfig = QRCodeConfig()


@hook_impl
@register_attr("config_models")
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


# @hook_impl
# def save(markata: "Markata") -> None:
#     filter_expr = markata.config.qrcode.filter
#     module_color = markata.config.qrcode.module_color
#     background = markata.config.qrcode.background
#     scale = markata.config.qrcode.scale
#
#     filtered_posts = markata.map("post", filter=filter_expr)
#
#     for post in filtered_posts:
#         # Create QR code from post URL
#         url = str(markata.config.url) + "/" + post.slug
#         qr = pyqrcode.create(url)
#
#         # Output file path
#         output_path = Path("markout") / post.slug / "qr.svg"
#         output_path.parent.mkdir(parents=True, exist_ok=True)
#
#         # Generate SVG with options
#         svg_kwargs = {
#             "module_color": module_color,
#             "background": background,
#         }
#
#         if scale > 0:
#             svg_kwargs["scale"] = scale
#         else:
#             svg_kwargs["omithw"] = True
#
#         qr.svg(str(output_path), **svg_kwargs)

from markata import background


@background.task
def render_qr(url, slug, module_color, background, scale):
    output_path = Path("markout") / slug / "qr.svg"
    if output_path.exists():
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)

    qr = pyqrcode.create(url)

    svg_kwargs = {
        "module_color": module_color,
        "background": background,
    }

    if scale > 0:
        svg_kwargs["scale"] = scale
    else:
        svg_kwargs["omithw"] = True

    qr.svg(str(output_path), **svg_kwargs)


def render_qr_job(post_data):
    output_path = Path("markout") / slug / "qr.svg"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        return

    url, slug, module_color, background, scale = post_data
    qr = pyqrcode.create(url)

    svg_kwargs = {
        "module_color": module_color,
        "background": background,
    }

    if scale > 0:
        svg_kwargs["scale"] = scale
    else:
        svg_kwargs["omithw"] = True

    qr.svg(str(output_path), **svg_kwargs)


@hook_impl
def post_render(markata: "Markata") -> None:
    filter_expr = markata.config.qrcode.filter
    module_color = markata.config.qrcode.module_color
    background = markata.config.qrcode.background
    scale = markata.config.qrcode.scale

    filtered_posts = markata.map("post", filter=filter_expr)
    futures = []
    for post in filtered_posts:
        futures.append(
            render_qr(
                str(markata.config.url) + "/" + post.slug,
                post.slug,
                module_color,
                background,
                scale,
            )
        )

    for future in futures:
        future.result()

    # with ThreadPoolExecutor() as executor:
    #     executor.map(
    #         lambda post: render_qr(
    #             str(markata.config.url) + "/" + post.slug,
    #             post.slug,
    #             module_color,
    #             background,
    #             scale,
    #         ),
    #         filtered_posts,
    #     )

    # cfg = markata.config.qrcode
    #
    # jobs = [
    #     (
    #         str(markata.config.url) + "/" + post.slug,
    #         post.slug,
    #         cfg.module_color,
    #         cfg.background,
    #         cfg.scale,
    #     )
    #     for post in filtered_posts
    # ]
    #
    # with ProcessPoolExecutor() as executor:
    #     executor.map(lambda args: render_qr_job(*args), jobs)
