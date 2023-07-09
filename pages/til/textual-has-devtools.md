---
date: 2022-06-09 21:21:11
templateKey: til
title: Textual has devtools
status: published
tags:
  - python
  - python
  - python
---

Textual has devtools in the upcoming css branch, and its pretty awesome!

## It's still early

Textual is still very early and not really ready for prime time, but it's quite
amazing how easy some things such as creating keybindings is. The docs are
coming, but missing right now so if you want to use textual be ready for
reading source code and examples.

## On to the devtools

As [@willmcgugan](https://twitter.com/willmcgugan) shows in this tweet it's
pretty easy to setup, it requires having two terminals open, or using tmux, and
currently you have to use the css branch.

<https://twitter.com/willmcgugan/status/1531294412696956930>

## Why does textual need its own devtools

Textual is a tui application framework. Unlike when you are building cli
applications, when the tui takes over the terminal in full screen there is no
where to print statement debug, and breakpoints don't work.

## getting the css branch

In the future it will likely be in main and not need this, but for now you need
to get the css branch to get devtools.

```bash
git clone https://github.com/Textualize/textual
git fetch --alll
git checkout css
```

## install in a virtual environment

Now you can create a virtual environment, feel free to use whatever virtual
environment tool you want, venv is built in to most python distributions
though, and should just be there.

```bash
python3 -m venv .venv --prompt textual
source .venv/bin/activate
pip install .
```

## Now that we have textual installed

Once textual is installed you can open up the devtools by running textual console.

```bash
textual console
```

![textual-console](https://screenshots.waylonwalker.com/textual-console.webp)
