---
date: 2022-10-11 14:34:35
templateKey: til
title: Markata Supports Jinja Plugins 0.5.0.dev2
status: 'draft'
tags:
  - python

---


## From the Changelog

The entry for 0.5.0.dev2 from markata's [changelog](https://markata.dev/changelog/)


* Created entrypoint hook allowing for users to extend marka with jinja
  exensions #60 0.5.0.dev2

## markata-gh

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

## Creating entrypoints in pyproject.toml

If your project is using `pyproject.toml` for packaging you can setup an entrypoint as follows.

``` toml
[project.entry-points."markata.jinja_md"]
markta_gh = "markata_gh.repo_list:GhRepoListTopic"
```

## Creating entrypoints in setup.py
