import hashlib
import re
import textwrap
from typing import TYPE_CHECKING, Dict, List

from markata.hookspec import hook_impl, register_attr
import json
from pathlib import Path

if TYPE_CHECKING:
    from markata import Markata

FENCED_BLOCK_RE = re.compile(
    textwrap.dedent(
        r"""
        (?P<fence>^(?:~{3,}|`{3,}))[ ]*                          # opening fence
        ((\{(?P<attrs>[^\}\n]*)\})|                              # (optional {attrs} or
        (\.?(?P<lang>[\w#.+-]*)[ ]*)?                            # optional (.)lang
        (hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot)[ ]*)?) # optional hl_lines)
        \n                                                       # newline (end of opening fence)
        (?P<code>.*?)(?<=\n)                                     # the code block
        (?P=fence)[ ]*$
        """
    ),
    re.MULTILINE | re.DOTALL | re.VERBOSE,
)


def find_codeblocks(article) -> List[Dict[str, str]]:
    codeblocks: List[Dict[str, str]] = []
    for block in FENCED_BLOCK_RE.findall(article):
        codeblocks.append(
            {
                "language": block[1],
                "code": block[9],
                "hash": hashlib.md5(block[9].encode("utf-8")).hexdigest(),
            }
        )
    return codeblocks


@hook_impl
@register_attr("codeblocks")
def render(markata: "Markata") -> None:

    markata.codeblocks = []
    for article in markata.iter_articles(description="creating codeblocks"):
        markata.codeblocks.extend(find_codeblocks(article.content))


@hook_impl
def save(markata: "Markata") -> None:
    output_file = Path(markata.config["output_dir"]) / "codeblocks.json"
    output_file.write_text(json.dumps(markata.codeblocks))
