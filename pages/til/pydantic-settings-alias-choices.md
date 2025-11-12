---
date: 2025-11-11 21:23:58
templateKey: til
title: pydantic settings alias choices
published: true
tags:
  - python

---

Today I learned how to use AliasChoices with pydantic settings to setup common
aliases for the same field.  I'm bad about remembering these things, and hate
looking up the docs.  I like things to be intuitive and just do the thing I
want it to do.  Especially when they get configured through something like yaml
and do not have a direct lsp look up right from my editor.  I figured out how
to support what might be common aliases for a storage directory.  These can be
set up as environment variables and used by config.

``` python
from pathlib import Path

from pydantic import Field
from pydantic import AliasChoices
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    storage_dir: Path | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "STORAGE_DIR", "STORAGE_DIRECTORY", "STORAGE_PATH", "STORAGE_PATHNAME",
            "DROPPER_STORAGE_DIR", "DROPPER_STORAGE_DIRECTORY", "DROPPER_STORAGE_PATH", "DROPPER_STORAGE_PATHNAME",
        ),
        description="Directory for stored files",
    )
```
