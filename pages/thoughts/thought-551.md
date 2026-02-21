---
title: '💭 Migration guide for config loaders — kedro 0.19.11 documentation'
date: 2025-02-05T18:16:44
template: link
link: https://docs.kedro.org/en/stable/configuration/config_loader_migration.html
tags:
  - kedro
  - thoughts
  - thought
  - link
published: true

---

![[https://docs.kedro.org/en/stable/configuration/config_loader_migration.html]]

Migrating from kedro 0.18.4 to the latest version involves handling the deprecated OmegaConf loader.  Switching over does not look as bad as I originally thought.


1. installing kedro 0.18.5+
2. set the CONFIG_LOADER_CLASS in settings.py
3. swap out import statements
4. config must be yaml or json
5. getting values from config must be done with bracket `__getattr__` style not with `.get`
6. any Exceptions caught from Templated config loader will need to be swapped to OmegaConfig exceptions, similar to #3
7. templated values must lead with an `_`
8. Globals are handled different
9. OmegaConfig does not support jinja2 sytax, but rather a `${variable}` syntax

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
