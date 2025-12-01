---
date: 2024-04-13 08:27:26
templateKey: til
title: Composing Typer clis
published: true
tags:
  - python

---

Typer makes it easy to compose your cli applications, like you might with a web
router if you are more familiar with that.  This allows you to build smaller
applications that compose into a larger application.

You will see similar patterns in the wild, namely the `aws` cli which always
has the `aws <command> <subcommand>` pattern.

Lets setup the cli app itself first.  You can put it in `project/cli/cli.py`.

``` python
import typer

from project.cli.api import api_app
from project.cli.config import config_app
from project.cli.user import user_app
from project.cli.run import run_app

app = typer.Typer()

app.add_typer(api_app, name="api")
app.add_typer(config_app, name="config")
app.add_typer(user_app, name="user")
app.add_typer(run_app, name="run")
```

Creating an app that will become a command is the same as creating a regular
app in Typer.  We need to create a callback that will become our command, and a
command that will become our subcommand in the parent app.

``` python
import typer
from rich.console import Console

from project.config import get_config

config_app = typer.Typer()

@config_app.callback()
def config():
    "model cli"


@config_app.command()
def show(
):
    project_config = get_config(env)
    Console().print(fokais_config)
```

Setting up the entrypoint in pyproject.toml.

``` toml
[project.scripts] # <- this project is part of the config DO NOT change it
project = "project.cli.cli:app" # <- This project is the project name, DO change it
```

Now you can see each cli application as a sub command.

``` bash
❯ project --help

 Usage: project [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion  [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell.│
│                                                        [default: None]                            │
│ --show-completion     [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell,   │
│                                                        to copy it or customize the installation.  │
│                                                        [default: None]                            │
│ --help                                                 Show this message and exit.                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────╮
│ api                        model cli                                                              │
│ config                     config cli                                                             │
│ user                       user cli                                                               │
│ run                        run cli                                                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```

In the example above we can run the command `project config show` to see the
current configuration of our project.
