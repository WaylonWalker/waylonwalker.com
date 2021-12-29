---
date: 2021-12-30T15:26:01
templateKey: til
title: My first impressions with pyenv
tags:
  - python
  - linux
  - bash

---

pyenv provides an easy way to install almost any version of python from
a large list of distributions. I have simply been using the version of
python from the os package manager for awhile, but recently I bumped my
home system to Ubuntu 21.10 impish, and it is only 3.9+ while the
libraries I needed were only compatable with up to 3.8.

> I needed to install an older version of python on ubuntu

I've been wanting to check out pyenv for awhile now, but without a
burning need to do so.

## List out install candidates

You can list all of the available versions to install with
`pyenv install --list`.  It does reccomend updating pyenv if you suspect
that it is missing one.  At the time of writing this comes out to 532
different versions!

``` bash
pyenv install --list
```

## Let's install the latest 3.8 patch

Installing a version is as easy as `pyenv install 3.8.12`.  This will
install it, but not make it active anywhere.

```
pyenv install 3.8.12
```

## let's use python 3.8.12 while in this directory

Running `pyenv local` will set the version of python that we wish to use
while in this directory and any directory underneath of it while using
the pyenv command.

``` bash
pyenv local python3.8.12
```

## .python-version file

This creates a `.python-version` files in the directory I ran it in,
that contains simply the version number.

``` bash
3.8.12
```

## using with pipx

I immediately ran into the same issue I was having before when trying to
run pipx, as pipx was running my system python.  I had to install pipx
in the python3.8 environment to get it to use it.

``` bash
pyenv exec pip install pipx
pyenv exec pipx run kedro new
```

## python is still the system python

When I open a terminal and call `python` its still my system python that
I installed and set with update-alternatives.  I am not sure if this is
expected or based on how I had installed the system python previously,
but it's what happened on my system.

```
update-alternatives --query python

Name: python
Link: /home/walkers/.local/bin/python
Status: auto
Best: /usr/bin/python3
Value: /usr/bin/python3
```

## making a virtual environment

To make a virtual environment, I simply ran `pyenv exec python` in place
of where I would normally run python and it worked for me.  There is a
whole package to get pyenv and venv to play nicely together, so I
suspect that there is more to it, but this worked well for me and I was
happy.

```
pyenv exec python -m venv .venv --prompt $(basename $PWD)
```

Now when my virtual environment is active it points to the python in
that virtual environment, and is the version of python that was used to
create the environment.

## Links
https://github.com/pyenv/pyenv#installation
