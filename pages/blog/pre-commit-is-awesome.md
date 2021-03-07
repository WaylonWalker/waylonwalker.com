---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: pre-commit is awesome
date: 2020-06-05T05:00:00.000+00:00
status: published
description: I recently discovered the ✨ awesomeness that is pre-commit. I steered
  away from it for so long because it seemed like a big daunting thing to set up,
  but really it's easy. It will automatically run checks for you. In some cases, it
  will even automatically fix them for you. Out of the box, it will do things like
  automatically trim extra whitespace, fix file endings, and ensure file sizes are
  not too large for git.
cover: "/static/pre-commit-is-awesome.png"

---
I recently discovered the ✨ awesomeness that is pre-commit. I steered away from it for so long because it seemed like a big daunting thing to set up, but really it's easy. It will automatically run checks for you. In some cases, it will even automatically fix them for you. Out of the box, it will do things like automatically trim extra whitespace, fix file endings, and ensure file sizes are not too large for git.

## Quickstart

It comes with a `sample-config` that is pretty general purpose and use for just about any project in git.

``` bash
pip instal pre-commit
pre-commit sample-config > .pre-commit-config.yaml
pre-commit install
git add .
git commit -m "added pre-commit"
```

## Cloned Repo

Once someone has created the `.pre-commit-config.yaml` everyone on the team will want to be running it for consistency's sake. (make sure everyone agrees with the config you have chosen first). Simply install the existing config.

``` bash
pip install pre-commit
git clone <repo>
pre-commit install
git add .
git commit -m "added pre-commit"
```

## sample-config

The sample configuration does some really basic, file ending, trailing-whitespace fixing. And checks for files too large for git. This one saved me when I tried to commit linux `rpm` once 🤦‍♀️.

``` yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.4.0
    hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml
    - id: check-added-large-files
```

## Adding some extras from pre-commit themselves

Here I have added a couple of extra ones form pre-commit

``` yaml
    - id: check-case-conflict # Check for files that would conflict in case-insensitive filesystems
    - id: check-merge-conflict # Check for files that contain merge conflict strings.
    - id: debug-statements # Check for debugger imports and py37+ `breakpoint()` calls in python source.
    - id: requirements-txt-fixer # Sorts entries in requirements.txt
    - id: forbid-new-submodules # Check for git submodules
    - id: flake8 # runs python flake8
```

The submodules one is big. I have seen several folks trying to learn git for the first time mistakenly start nesting all of their projects underneath each other and eventually losing a lot of work. Trying to learn the command line and git all at once can be really confusing.

## skip pre-commit

So you have a big codebase and you are trying to get pre-commit ready, but you just need your changes in.

``` yaml
git commit -m "commiting wihout pre-commit" --no-verify
```

## manually run pre-commit

If you have an existing repo and want to run pre-commit on everything, since it was pre-existing, you can do that manually.

``` yaml
pre-commit run --all-files
```

## So pre-commit changed some files

Since `pre-commit` only runs against staged files, but makes changes to the local files you need to add them.

Here is a git status after committing with some trailing whitespace issues.

``` bash
❯ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified: README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified: README.md
```

`pre-commit` will keep yelling at you about `trailing whitespace` until you add the files.

``` bash
git add README.md
```

## Community Developed plugins

_give me more_

These almost make it **too** easy. Sharing your process to get up and running without `pre-commit` can involve a lot of instructions. Installing several different tools, then running them manually, probably forgetting to do so sometimes. These will automatically install and only run scoped to the files that have changed, not on the whole repo.

### isort

``` yaml
- repo: https://github.com/asottile/seed-isort-config
rev: v2.1.1
hooks:
    - id: seed-isort-config
- repo: https://github.com/pre-commit/mirrors-isort
rev: v4.3.21
hooks:
    - id: isort
```

### .isort.cfg

In order to get isort to play nicely with black, I found great success with the following config placed in the root of the repo at `.isort.cfg`. Without these settings, I found that you commits will consistently fail checks because `isort` and `black` are fighting each other.

``` toml
[settings]
multi_line_output=3
include_trailing_comma=True
force_grid_wrap=0
use_parentheses=True
line_length=88
```

### .flake8

Just as with `isort` flake8 tends to complain about a few things that black does. To get them to play nicely together place this file in the root of the repo at `.flake8`.

``` toml
# taken from black
# added E231 as is conflicts with black formatting
[flake8]
ignore = E203, E266, E501, W503, E231, F541
max-line-length = 88
max-complexity = 18
select = B,C,E,F,W,T4,B9
```

### black

Black is an amazing CLI tool the python community has been blessed with. It was developed by python core dev Lukasz Langa after deep research of real python projects. It will autoformat your project and will check that the AST before and after remains the same ensuring that the code will run exactly the same. It only makes it more readable. I keep black installed and set to run on save. Many times I will bang out some sloppy code with long lines or poor indentation hit save and let black take care of the easy work.

``` yaml
- repo: https://github.com/asottile/blacken-docs
    rev: v1.7.0
    hooks:
        - id: blacken-docs
        - additional_dependencies: [black]
- repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
        - id: black
```

### mypy

I have recently fallen in love with mypy. It has saved me from shipping some bugs that would not have been caught with tests, even with 100% coverage. I don't have 100% coverage across every possible type entered.

``` yaml
    - repo: https://github.com/pre-commit/mirrors-mypy
      rev: v0.720
      hooks:
          - id: mypy
            exclude: tests/
```

## Your own plugin

Sometimes you have a CLI tool that you want to run, but there is no plugin. No worries, you can install manually set the repo to local, and add an entry for your CLI command to run.

``` yaml
    - repo: local
      hooks:
          - id: interrogate
   		  name: "Interrogate docstring coverage check"
          types: [file, python]
          entry: interrogate -f 100 -vv
```

***

I have been writing short snippets about my mentality breaking into the tech/data industry in my newsletter, 👇 check it out and lets get the conversation started.

[![Sign up for my Newsletter](https://images.waylonwalker.com/waylon-walker-newsletter.png)](https://waylonwalker.com/newsletter)
