---
date: 2022-09-02 07:54:03
templateKey: til
title: Create a new Python Project with the Hatch Cli
published: true
tags:
  - python
cover: https://images.waylonwalker.com/hatch-new.png

---

I'm really getting into using hatch as my go to build system, and I am really
liking it so far.  I am slowly finding new  things that just work really well.
`hatch new` is one of those things that I didn't realize I needed until I had
it.


![Hatch new cover image](https://images.waylonwalker.com/hatch-new.png)

> creating new versions created by myself with stable diffusion

![hatch-new-cli](https://screenshots.waylonwalker.com/hatch-new-cli.webp)


```
❯ pipx run hatch new --help
Usage: hatch new [OPTIONS] [NAME] [LOCATION]

  Create or initialize a project.

Options:
  -i, --interactive  Interactively choose details about the project
  --cli              Give the project a command line interface
  --init             Initialize an existing project
  -h, --help         Show this message and exit.
```

> Note! I am running all of these commands with pipx. I like to use pipx for
> all of my system level cli applications.  To emphasis this point in the
> article I am going to use `pipx run hatch`, but you can `pipx install hatch`
> then just run `hatch` from there.

## Interacively create a new project

Running `hatch new -i` will ask let you interactivly choose details about the
project, such as the project's name.

```
pipx run hatch new -i
```

After running and naming the project **Hatch New** we end up with the following
filetree.

``` bash
❯ tree .
.
├── hatch_new
│   ├── __about__.py
│   └── __init__.py
├── LICENSE.txt
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py
```

## Non-Interative

You can also fill in the project name ahead of time, and it will run without
any questions.

![hatch-new-another-project](https://screenshots.waylonwalker.com/hatch-new-another-project.webp)

``` bash
❯ pipx run hatch new "Another Project"
another-project
├── another_project
│   ├── __about__.py
│   └── __init__.py
├── tests
│   └── __init__.py
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

> Note! all of these examples will create a project directory within your
> current working directory.

!["An astronaut working in a lab, there is a series of eggs ready to hatch baby snakes on the table, experiments running, beakers, test tubes, cyberpunk, octane render, trending on artstation, neon lighting, volumetric lighting, pink lighting" -s50 -W800 -H450 -C10.0 -Ak_lms -S324995023](https://stable-diffusion.waylonwalker.com/000146.324995023.webp)

## --init
_existing project_

`hatch new` has an `--init` flag in order to initialize a new hatch
pyproject.toml in an existing project.  This feels like it would be useful if
you are converting a project to hatch, or if like me you sometimes start making
something before you realize it's something that you want to package.  Honestly
this doesn't happen too much anymore I package most things, and I hope `hatch
new` completely breaks this habbit of mine.

Let's say I have the following existing project.

``` bash
❯ tree
.
└── hatch_init
    └── __init__.py

1 directory, 1 file
```

I can setup packaging with hatch by running.

``` bash
pipx run hatch new --init
```

![hatch-init-existing](https://screenshots.waylonwalker.com/hatch-init-existing.webp)


The `pyproject.toml` that comes out is pretty similar to the one that comes out
of the normal `hatch new`, but without any other files.

> Note that you will need to setup a `__about__.py` yourself for the dynamic
> versioning that it has setup for you.

``` toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "hatch-init"
description = 'initialize an existing project using hatch'
readme = "README.md"
requires-python = ">=3.7"
license = "MIT"
keywords = []
authors = [
  { name = "Waylon S. Walker", email = "waylon@waylonwalker.com" },
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]
dependencies = []
dynamic = ["version"]

[project.urls]
Documentation = "https://github.com/unknown/hatch-init#readme"
Issues = "https://github.com/unknown/hatch-init/issues"
Source = "https://github.com/unknown/hatch-init"

[tool.hatch.version]
path = "hatch_init/__about__.py"

[tool.hatch.envs.default]
dependencies = [
  "pytest",
  "pytest-cov",
]
[tool.hatch.envs.default.scripts]
cov = "pytest --cov-report=term-missing --cov-config=pyproject.toml --cov=hatch_init --cov=tests"
no-cov = "cov --no-cov"

[[tool.hatch.envs.test.matrix]]
python = ["37", "38", "39", "310", "311"]

[tool.coverage.run]
branch = true
parallel = true
omit = [
  "hatch_init/__about__.py",
]

[tool.coverage.report]
exclude_lines = [
  "no cov",
  "if __name__ == .__main__.:",
  "if TYPE_CHECKING:",
]
```

## cli

`hatch new` does not stop there, it also has a `--cli` flag to give you a cli
out of the box as well.

``` bash
❯ pipx run hatch new "new cli" --cli
new-cli
├── new_cli
│   ├── cli
│   │   └── __init__.py
│   ├── __about__.py
│   ├── __init__.py
│   └── __main__.py
├── tests
│   └── __init__.py
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

When you use the `--cli` flag you also get `click` as a dependency and
`project.scripts` setup automatically.

```
[project]
name = "new-cli"

# ...

dependencies = [
  "click",
]

# ...

[project.scripts]
new-cli = "new_cli.cli:new_cli"
```

!["An astronaut working in a lab, there is a series of eggs ready to hatch baby snakes on the table, experiments running, beakers, test tubes, cyberpunk trending on artstation" -s50 -W800 -H450 -C7.5 -Ak_lms -S98801549
](https://stable-diffusion.waylonwalker.com/000130.98801549.webp)

## what's in the cli

It's a hello-world click application.

``` python
# SPDX-FileCopyrightText: 2022-present Waylon S. Walker <waylon@waylonwalker.com>
#
# SPDX-License-Identifier: MIT
import click

from ..__about__ import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='new cli')
@click.pass_context
def new_cli(ctx: click.Context):
    click.echo('Hello world!')
```

## sneak peek

I'll dive more into environments and the run command later, but we can run the
cli pretty damn quick with two commands. In under 5s I was able to run this cli
that it created.  This is a pretty incredible startup time.


![pipx-run-hatch-hello-world](https://screenshots.waylonwalker.com/pipx-run-hatch-hello-world.webp)

!["An astronaut working in a lab, there is a series of eggs ready to hatch baby snakes on the table, experiments running, beakers, test tubes, cyberpunk trending on artstation, neon lighting, volumetric lighting, pink lighting" -s50 -W800 -H450 -C7.5 -Ak_lms -S2274808816](https://stable-diffusion.waylonwalker.com/000136.2274808816.webp)
