from typing import TYPE_CHECKING, List, Optional

import pydantic
from markata.hookspec import hook_impl, register_attr

if TYPE_CHECKING:
    from markata import Markata


class Post(pydantic.BaseModel):
    templateKey: str
    tags: Optional[List[str]] = []

    @pydantic.validator("tags", pre=True, always=True)
    def default_tags(cls, v, *, values):
        if v is None:
            return []
        if isinstance(v, list):
            return v
        if isinstance(v, str):
            return [v]


@hook_impl(trylast=True)
@register_attr("post_models")
def post_model(markata: "Markata") -> None:
    markata.post_models.append(Post)
