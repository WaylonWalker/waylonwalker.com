---
date: 2022-10-06 18:25:10
templateKey: til
title: Markata now uses hatch
status: 'draft'
tags:
  - python

---

Markata now uses hatch as its build backend, and version bumping tool.
`setup.py`, and `setup.cfg` are completely gone.

## 0.5.0 is big

Markata 0.5.0 is now out, and it's huge.  Even though it's the backend of this
blog I don't actually have that many posts directly about it.  I've used it a
bit for blog fuel in generic ways, like talking about pluggy and diskcache, but
very little have I even mentioned it.

Over the last month I made a big push to get 0.5.0 out, which adds a whole
bunch of new configurability to `markata`.

Here's the [changelog](https://markata.dev/changelog/) entry.

> * Moved to PEP 517 build #59 0.5.0.dev1

## My Personal Simple CI/CD

Before cutting all of my personal projects over to hatch.  The first thing I
did was to setup a solid github action,
[hatch-action](https://github.com/WaylonWalker/hatch-action)that I can resue.

It automatically bumps versions, using pre-releases on all branches other than
main, with special branches for bumping major, minor, patch, dev, alha, beta,
and dev.

## hatch new --init

To convert the project over to hatch, and get rid of setup.py/setup.cfg, I ran
`hatch new --init`.  This automatically grabs all the metadata for the project
and makes a `pyproject.toml` that has most of what I need.

``` bash
hatch new --init
```

I then manually moved over my isort config, put flake8 config into `.flake8`,
and dropped setup.cfg.

## lint-test

Part of my hatch-action is to run a `before-command`, for markata, this runs
all of my linting and testing in one hatch script called `lint-test`.  If this
fails CI will fail and I can read the report in the logs, make a fix and
re-publish.

``` toml
[tool.hatch.envs.default.scripts]
cov = "pytest --cov-report=term-missing --cov-config=pyproject.toml --cov=markata --cov=tests"
no-cov = "cov --no-cov"
lint = "flake8 markata"
format = "black --check markata"
sort-imports = "isort markata"
build-docs = "markata build"
lint-test = [
 "lint",
 "format",
 "seed-isort-config",
 "sort-imports",
 "cov",
]
test-lint = "lint-test"
```

## Typical branching workflow
_with automatic versioning_

My typical workflow is to work on features in their own branch where they do
not automatically version or publish, they keep the same version they were
branched off of.  Then I do a pr to develop, which will do a `minor,dev` bump
and publish a pre-relese to pypi.

``` text
# starting with version 0.0.0
Feature1 -- │
Feature2 -- ├── dev 0.1.0.dev1,2,3 ── main 0.1.0
Feature3 -- │
```

I will let several features collect in develop before cutting a full relese
over to main.  This gives me time to make sure the solution is what makes the
most sense, I try to use it in a few projects, and generally its edges show,
and another pr is warranted to make the feature useful for more use cases.
After running and using these new releases in a few projects, I am confident
that its ready and release to main.

### managing prs

Doing PR's with gh, probably deserves its own post but here are some helpful
commands.

``` bash
gh pr create --base develop --fill
gh pr edit
gh pr diff | dunk
gh pr merge -ds
```

## Building and publishing

hatch makes building and publishing pretty straightforward.  It's one command
inside my hatch-action to build and one to publish.  On each project that uses
my hatch-action I only need to give it a token that I get from PyPi.

``` yaml
env:
  HATCH_INDEX_USER: __token__
  HATCH_INDEX_AUTH: ${{ secrets.pypi_password }}
```

## Full set of changes

If you want to see all of the details on how markata moved over to hatch, you can check out this diff.

https://github.com/WaylonWalker/markata/compare/v0.4.0..v0.5.0.dev0
