---
date: 2022-10-11 14:34:35
templateKey: til
title: Markata Supports Jinja Plugins 0.5.0.dev2
published: true
jinja: false
tags:
  - python
  - markata
---

Markata now allows you to create jinja extensions that will be loaded right in
with nothing more than a `pip install`.

## From the Changelog

The entry for 0.5.0.dev2 from markata's [changelog](https://markata.dev/changelog/)

* Created entrypoint hook allowing for users to extend marka with jinja
  exensions #60 0.5.0.dev2

!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S1808537114](https://stable-diffusion.waylonwalker.com/000368.1808537114.webp){.more-cinematic}

## markata-gh

The first example that you can use right now is `markata-gh`.  It will render
repos by GitHub topic and user using the gh cli, which is available in github
actions!

Get it with a pip install

``` bash
pip install markata-gh
```

Use it with some jinja in your markdown.

``` markdown
## Markata plugins

It uses the logged in uer by default.

{% gh_repo_list_topic "markata" %}

You can more explicitly grab your username, and a topic.
{% gh_repo_list_topic "waylonwalker", "personal-website" %}
```

## How is this achieved

The jinja extension details are for another post, but this is how `markata-gh`
exposes itslef as a jinja extension.

``` python
class GhRepoListTopic(Extension):
    tags = {"gh_repo_list_topic"}

    def __init__(self, environment):
        super().__init__(environment)

    def parse(self, parser):
        line_number = next(parser.stream).lineno
        try:
            args = parser.parse_tuple().items
        except AttributeError:
            raise AttributeError(
                "Invalid Syntax gh_repo_list_topic expects <username>, or <username>,<topic> both must have the comma"
            )

        return nodes.CallBlock(self.call_method("run", args), [], [], "").set_lineno(
            line_number
        )

    def run(self, username=None, topic=None, caller=None):
        "get's markdown to inject into post"
        return repo_md(username=username, topic=topic)
```

!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S2487720618 ](https://stable-diffusion.waylonwalker.com/000368.2487720618.webp)

## Entrypoints

Then `markata-gh` exposes itself as an extension through entrypoints.

### Creating entrypoints in pyproject.toml

If your project is using `pyproject.toml` for packaging you can setup an
entrypoint as follows.

``` toml
[project.entry-points."markata.jinja_md"]
markta_gh = "markata_gh.repo_list:GhRepoListTopic"
```

## Creating entrypoints in setup.py

If your project is using `setup.py` for packaging you can setup an
entrypoint as follows.

``` python
setup(
    ...
    entry_points={
        "markata.jinja_md": ["markta_gh" = "markata_gh.repo_list:GhRepoListTopic"]
    },
    ...
)
```

!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S655826089](https://stable-diffusion.waylonwalker.com/000368.655826089.webp)
