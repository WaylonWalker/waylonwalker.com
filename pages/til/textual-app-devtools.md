---
date: 2022-10-24 07:42:48
templateKey: til
title: textual app devtools
status: published
tags:
  - python
---

I am working through the textual tutorial, and I want to put it in a proper cli
that I can pip install and run the command without `textual run --dev app.py`.
This is a fine pattern, but I also want this to work when I don't have a file
to run.

!["An astronaut working in a lab, hacking on a computer terminal, htop is running, shallow depth of field beakers, test tubes, volumetric lighting, pink lighting, by victo ngai, killian eng vibrant colours, dynamic lighting, digital art" -s50 -W768 -H448 -C7.5 -Ak_lms -S3617210203](https://stable-diffusion.waylonwalker.com/000221.3617210203.webp)

## pyproject.toml entrypoints

I set up a new project running `hatch new`, and added the following entrypoint,
giving me a `tutorial` cli command to run.

```toml
...

[project.scripts]
tutorial = 'textual_tutorial.tui:tui'
```

<https://waylonwalker.com/hatch-new-cli/>

## setup.py entrypoints

If you are using `setup.py`, you can set up entrypoints in the `setup` command.

```python
from setuptools import setup

setup(
    ...
    entry_points={
        "console_scripts": ["tutorial = textual_tutorial.tui:tui"],
    },
    ...
)
```

<https://waylonwalker.com/minimal-python-package/>

## tui.py

_adding features_

Now to get devtools through a cli without running through `textual run --dev`.
I pulled open the textual cli source code, and this is what it does currently.

> Note: I used sys.argv as a very simple way to implement a `--dev` flag in the
> tutorial. For a real project, I'd setup argparse, click, or typer. `typer`
> is my go to these days, unless I am really trying to limit dependencies, then
> the standard library `argparse` might be what I go with.

```python
def tui():

    from textual.features import parse_features
    import os
    import sys

    dev = "--dev" in sys.argv # this works, but putting it behind argparse, click, or typer would be much better

    features = set(parse_features(os.environ.get("TEXTUAL", "")))
    if dev:
        features.add("debug")
        features.add("devtools")

    os.environ["TEXTUAL"] = ",".join(sorted(features))
    app = StopwatchApp()
    app.run()


if __name__ == "__main__":
    tui()
```

## Other Flags???

If you look at the source, there is one other flag for `headless` mode.

```python
FEATURES: Final = {"devtools", "debug", "headless"}
```

## Run it

Here it is running with `tutorial --dev` on the left, and `textual console` on the right.

![textual-tutorial-devtools](https://screenshots.waylonwalker.com/textual-tutorial-devtools.webp)
