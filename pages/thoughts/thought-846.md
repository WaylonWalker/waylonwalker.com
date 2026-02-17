---
title: '💭 PEP 735 – Dependency Groups in pyproject.toml | peps.python.org'
date: 2025-10-01T16:25:57
templateKey: link
link: https://peps.python.org/pep-0735/
tags:
  - python
published: true

---

> PEP 735 describes dependency groups as sets of optional dependencies that are not shipped with the package but intended for development purposes.

The PEP includes an example for groups that include test, docs, typing, and a combo typing-test.

``` toml
[dependency-groups]
test = ["pytest", "coverage"]
docs = ["sphinx", "sphinx-rtd-theme"]
typing = ["mypy", "types-requests"]
typing-test = [{include-group = "typing"}, {include-group = "test"}, "useful-types"]
```

This is implemented in uv and can be used by several of their commands.

``` bash
uv sync --group test
uv run --group test
uv add --group test pytest
uv remove --group test pytest
uv export --group test
uv tree --group test
```

## Dependency Groups are not Extras

The docs describe extras as being intended to ship with the application and dependency groups intended for development.  The spec allows both to exist with the same name, but care should be taken as tools may have different implementations.

>  Tools MAY choose to provide the same interfaces for installing Dependency Groups as they do for installing extras.
>
> Note that this specification does not forbid having an extra whose name matches a Dependency Group.
>
> Users are advised to avoid creating Dependency Groups whose names match extras. Tools MAY treat such matching as an error.

[Original thought](https://peps.python.org/pep-0735/)
