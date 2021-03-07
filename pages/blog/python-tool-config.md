---
templateKey: blog-post
tags: ['python']
title: ⚙ How Python Tools Are Configured
date: 2021-01-21T00:00:00
status: draft

---

There are various ways to configure python tools, config files, code, or
environment variables.  Let's look at a few projects that allow users to
configure them through the use of config files and how they do it.

## Motivation

This will not include how they are implemented, I've looked at a few and its
not simple.  This will focus on where config is placed and the order in which
duplicates are resolved.

The motivation of this article is to serve as a bit of a reference guide for
those who may want to create their own package that needs configuration.

## Flake8

### Global

User settings can exist in the users `~/.config/flake8` file to configure how
flake8 runs on their machine.

* `~/.config/flake8`

### Per-Project

Only One project config file will be considered, but allows for several
options.  These files all use the `ini` format and must have a `[flake8]`
section  header to be consideered.

Selection of the config file can also be overridden by the `--config` cli option.

An extra config file may be selected as `--append-config`.  It will be read in
last and take highest precedence.

* `tox.ini`
* `setup.cfg`
* `.pep8`
* `.flake8`

## Example Config

_valid in any of the supported files_

``` ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

### Options

The number of options configured through config files is fairly short for `flake8`.

* exclude
* filename
* select
* ignore
* max-line-length
* format
* max-complexity

## Black

Black only supports `TOML` file formats for configuration.

### Global

Black provides no global config support.  If you really needed one I guess you
could make a cli alias.

### Per-Project

Black states that it includes sane defaults that do not need configured, but if
you need to do so it only supports `pyproject.toml` or cli arguments.

Personally I believe that a lot of work went into making these sane defaults
really good.  I personally do not make any configuration changes to black.

* pyproject.toml

## Example

_pyproject.toml_

``` toml
[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```

## Resolution

Black will use teh `pyproject.toml` file for configuration, then make any
addional overrides through the use of command line arguments.

## MyPy

`mypy` takes the cake for the most complex configuration.  Primarily because
you can configure how it treats different modules specifically.  These modules
may be inside your codebase or installed and imported in.

### Per-Project

* --config-file
* mypy.ini
* .mypy.ini

### Global

* $XDG_CONFIG_HOME/mypy/config
* ~/.config/mypy/config
* ~/.mypy.ini

### Resolution

* --config-file
* mypy.ini
* .mypy.ini
* setup.cfg
* $XDG_CONFIG_HOME/mypy/config
* ~/.config/mypy/config
* ~/.mypy.ini

### Example
_mypy.ini_

```
# Global options:

[mypy]
python_version = 2.7
warn_return_any = True
warn_unused_configs = True

# Per-module options:

[mypy-mycode.foo.*]
disallow_untyped_defs = True

[mypy-mycode.bar]
warn_return_any = False

[mypy-somelibrary]
ignore_missing_imports = True
```

## Kedro - framework

Kedro is a unique one here.  It offers two distinctly different configurations,
one for how the framework behaves and the other for actual project config.

Kedro does utilizes a `settings.py` and `pyproject.toml` to define a bit more
of the framework settings.  These are the outter layer of your project.


These files sit at the root of the project.

### [pyproject.toml](https://github.com/quantumblacklabs/kedro/blob/fb88cc2504ddbfc93b9b859ca436130b396b93c4/docs/source/12_faq/02_architecture_overview.md#pyprojecttoml)

This replaces much of what used to be specified in run.py.

* package_name
* project_name
* project_version
* source_dir

### [Settings.py](https://github.com/quantumblacklabs/kedro/blob/fb88cc2504ddbfc93b9b859ca436130b396b93c4/docs/source/12_faq/02_architecture_overview.md#settingspy)

* DISABLE_HOOKS_FOR_PLUGINS
* HOOKS
* SESSION_STORE_CLASS
* SESSION_STORE_ARGS
* CONTEXT_CLASS

## Kedro - project

Within the project generally in the `src/conf` directory kedro allows you to
set both local and base configurations.  Local configurations will be git
ignored and most commonly used for credentials.

* catalog
* logging
* credentials


### Config Loader

Kedro lets you setup the config loader if you choose to do so.  You can
configure the directories to look in as well as the glob pattern for files.

``` python
from kedro.config import ConfigLoader

conf_paths = ["conf/base", "conf/local"]
conf_loader = ConfigLoader(conf_paths)
conf_catalog = conf_loader.get("catalog*", "catalog*/**")
```

### additional envs

Additional to the `base` and `local` config, kedro lets you specify an env at
runtime through a `--env` argumet or a `KEDRO_ENV` variable.  setting this will
additionally tell kedro to reach into `conf/<env-name>` for configuration.

### Resolution Order

kedro will load each config starting from `base`, `local`, then `env` and will
overrite any colllisions along the way.


**precedence heirarchy**

* env
* local
* base

### Jinja Support

As of `0.17.0` kedro supports jinja2 templates in its yml configuration files.
This is quite beneficial as catalogs can become incredebly repetative.

``` yaml
{% for speed in ['fast', 'slow'] %}
{{ speed }}-trains:
    type: MemoryDataSet

{{ speed }}-cars:
    type: pandas.CSVDataSet
    filepath: s3://${bucket_name}/{{ speed }}-cars.csv
    save_args:
        index: true

{% endfor %}
```

## pytest

Currently pytest is configured 

## resolution order

`pytest` will look for the existence of each of these files, if its a match it
will stop looking for new files, even if the file is empty.

* `pytest.ini`
* `pyproject.toml` with `[tool.pytest.ini_options]`
* `tox.ini` with `[pytest]`
* `setup.cfg` with `[tool:pytest]`

## Multiple Config

`pytest` is a bit unique here in that it allows for multiple configs.  There is
a complex resolution for module specific configuration, but essentially it does
the resolution highlighted above through a number of directories and returns
the config closest to the test module.

## Example pytest config


``` ini
# pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
```

## Command Line Options

As far as I am aware every option specified in a config file can also be
configured or overridden at the command line.

## ipython

`Ipython` is configured completely at a system level with python scripts within
the users `~/.ipython/` directory.  The user may have multiple profiles that
can be created by running `ipython profile create [profilename]` or specified
by running `ipython --profile=[profilename]`

### Config Directory

By default this is `~/.ipython`, but an be configured by setting the
`IPYTHONDIR` environment variable or `--ipython-dir=<path>` command line
option.

### Example Config

``` python
# sample ipython_config.py
c = get_config()

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 20
c.InteractiveShellApp.extensions = [
    'myextension'
]
c.InteractiveShellApp.exec_lines = [
    'import numpy',
    'import scipy'
]
c.InteractiveShellApp.exec_files = [
    'mycode.py',
    'fancy.ipy'
]
c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.deep_reload = True
c.InteractiveShell.editor = 'nano'
c.InteractiveShell.xmode = 'Context'

c.PromptManager.in_template  = 'In [\#]: '
c.PromptManager.in2_template = '   .\D.: '
c.PromptManager.out_template = 'Out[\#]: '
c.PromptManager.justify = True

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
 ('la', 'ls -al')
]
```

### CommandLine Overrides

Every configurable value can be overridden from the command line.

``` bash
ipython --ClassName.attribute=value
```

### Config Magic

Configuration can be overridden at runtime with the `%config` magic.

``` python
%config IPCompleter.greedy = True
```

### Startup

Every ipython profile has a startup directory where it will execute each `.py`
and `.ipy` file on startup.  You can make additional configuration here, import
modules you want readily available, execute literally any python code you want
to at the startup of that particular profile.
