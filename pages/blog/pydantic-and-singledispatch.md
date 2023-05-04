---
date: 2023-05-03 17:31:13
templateKey: blog-post
title: Pydantic and singledispatch
tags:
  - python
  - python
  - python
status: published
---

I was reading about
[pydantic-singledispatch](https://www.gidware.com/reducing-complexity-with-pydantic-singledispatch/)
from Giddeon's blog and found it very intersting. I'm getting ready to
implement pydantic on my static site generator [markata](https://markata.dev/),
and I think there are so uses for this idea, so I want to try it out.

## The Idea

Let's set up some pydantic settings. We will need separate Models for each
environment that we want to support for this to work. The whole idea is to use
`functools.singledispatch` and type hints to provide unique execution for each
environment. We might want something like a path_prefix in prod for
environments like GithubPages that deploy to `/<name-of-repo>` while keeping
the root at `/` in dev.

## Settings Model

Here is our model for our settings. We will create a CommonSettings model
that will be used by all environments. We will also create a `DevSettings`
model that will be used in dev and `ProdSettings` that will be used in prod.
We will use `env` as the discriminator so pydantic knows which model to use.

```{.python .darkmark}
from typing import Literal, Union

import pydantic
from pydantic import Field
from rich import print
from typing_extensions import Annotated


class CommonSettings(pydantic.BaseSettings):
    """Common settings for all environments"""
    debug: bool = False
    secret_key: str = "secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60


class DevSettings(CommonSettings):
    """Settings for dev"""
    env: Literal["dev"]


class ProdSettings(CommonSettings):
    """Settings for prod"""
    env: Literal["prod"]


class Settings(pydantic.BaseSettings):
    """Settings for all environments"""
    __root__: Annotated[Union[DevSettings, ProdSettings], Field(discriminator="env")]

    class Config:
        env_prefix = "APP_"



# Create our settings
settings = Settings(__root__={"env": "dev"}).__root__
# or
settings = Settings.parse_obj({"env": "dev"}).__root__
print(settings)
```

```{.console .darkmark_output}
DevSettings(debug=False, secret_key='secret', algorithm='HS256', access_token_expire_minutes=60, env='dev')
```

## Singledispatch

Now let's create our `where_am_i` function. We will use `functools.singledispatch`
to provide a unique execution for each environment. It will leverage type
hints to provide a unique execution for each environment.

```{.python .darkmark}
from functools import singledispatch

@singledispatch
def where_am_i(obj):
   '''
   Where am I?
   '''

@where_am_i.register
def dev(obj: DevSettings):
   '''
   Where am I?
   '''
   print('I am in dev')

@where_am_i.register
def prod(obj: ProdSettings):
   '''
   Where am I?
   '''
   print('I am in prod')


```

```{.console .darkmark_output}

```

## Output

Let's call our eample function `where_am_i` with our settings and see the
results.

```{.python .darkmark}
where_am_i(settings)
```

```{.console .darkmark_output}
I am in dev
```

```{.python .darkmark}
where_am_i(Settings.parse_obj({'env': 'prod'}).__root__)
```

```{.console .darkmark_output}
I am in prod
```

## Environment Variables

So far one down side to the TaggedUnion technique is that I am unable to pull
env from environment variables. I'm sure there is a way around this with a
different model design. Maybe following exactly what Giddeon did.

```{.python .darkmark}
os.environ.clear()
os.environ['APP_ENV'] = 'prod'
where_am_i(Settings().__root__)
```

```console
ValidationError: 1 validation error for Settings
__root__
  field required (type=value_error.missing)
<darkmark.darkmark.DarkMark object at 0x7fcc58bec5d0>
```

## FIN

I'm really digging pydantic lately and excited to get it built into
[markata](https://markata.dev/). Not 100% sure if I have a
