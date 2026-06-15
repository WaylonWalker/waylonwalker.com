---
templateKey: blog-post
tags: ['python', 'cli']
title: simple click
date: 2020-01-29T06:00:00.000+00:00
published: true
description: Add helpful cli to your python libraries... All of them!

---
cli tools are super handy and easy to add to your python libraries to supercharge them. Even if your library is not a cli tool there are a number of things that a cli can do to your library.

## Example Ideas

Things a cli can do to enhance your library.

🆚 print version
🕶 print readme
📝 print changelog
📃 print config
✏ change config
👩‍🎓 run a tutorial
🏗 scaffold a project with cookiecutter

## 🖱 [Click](https://click.palletsprojects.com/)

[Click](https://click.palletsprojects.com/) is the most popular python cli tool framework for python. There are others, some old, some new comers that make take the crown. For now [Click](https://click.palletsprojects.com/) is the gold standard if you want to make a powerful cli quickly. If you are dependency conscious and dont need a lot of tooling, use [argparse](https://docs.python.org/3/library/argparse.html).

## Project Structure

    .
    ├── setup.py
    └── simple_click
        ├── cli.py
        └── __init__.py

## ❯ cli.py

``` python
    # simple_click/cli.py
    import click

    __version__ = "1.0.0"

    @click.group()
    def cli():
       pass

    @cli.command()
    def version():
        """prints project version"""
        click.echo(__version__)


    if __name__ == '__main__':
        cli()
```

## ✨ **init**.py

For our simple_click library `__init__.py__` can be left empty. It is here purely to signify that simple_click is a library. It is likely that you will import other modules here that need to reside at the top level of your library api, your cli does not need to be at the top of of your api.

``` python
    # __init__.py
```

## 🚪 Entry Points

Entry points are the magic that make python cli tools available as their own command without having python before it or the file extension.

``` python
    # setup.py

    from setuptools import setup, find_packages

    # this is the 🥩 meat of this snippet
    # simple_click is the command name
    # = simple_click is the library name
    # .cli is the cli.py file
    # :cli is the cli function
    #
    # the second item is a shorthand alias to the main command

    entry_points = [
       "simple_click = simple_click.cli:cli",
       "scli         = simple_click.cli:cli",
    ]


    setup(
        name='simple_click',
        version='1.0.0',
        url='https://github.com/mypackage.git',
        packages=find_packages(),
        entry_points={"console_scripts": entry_points},

    )
```

## 🕶 See it in action

![Simple-click-in-action](https://dropper.wayl.one/file/fadd503a-0ae8-42eb-9c53-628c26424631.mp4)

## 📢 Discuss

What do You wish more python libraries included in their cli?  [Tweet it @_waylonwalker](https://twitter.com/intent/tweet?text=@_waylonwalker%20More%20libraries%20should%20...%0A%0Awaylonwalker.com/b/scli)

![Tweet it @_waylonwalker](https://twitter.com/intent/tweet?text=@_waylonwalker%20More%20libraries%20should%20...%0A%0Awaylonwalker.com/b/scli)
