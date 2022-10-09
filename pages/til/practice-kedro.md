---
templateKey: til
title: Practice making pipelines with kedro
date: 2022-01-27T21:07:37
tags:
    - python
    - kedro

---

I am a huge believer in practicing your craft.  Professional athletes
spend most of their time honing their skills and making themsleves
better.  In Engineering many spend nearly 0 time practicing.  I am not
saying that you need to spend all your free time practicing, but a few
minutes trying new things can go a long way in how you understand what
you are doing and make a hue impact on your long term productivity.


https://waylonwalker.com/what-is-kedro/

## Start practicing

**practice** building pipelines with _#kedro_ today

Go to your playground directory, and if you don't have one, make one.

``` bash
cd ~/playground
```

## get pipx

Install pipx in your system python.  This is one of the very few, and
possibly the only python library that deserves to be installed in your
system directory, primarily because its used to sanbox clis in their own
virtual environment automatically for you.

``` bash
pip install pipx
```

## make a new project

From inside your `playground` directory, start your new kedro project.
This is quite simple and painless.  So much so that if you mess this one
up doing something wild, it might be easier to make a new one that
fixing the wild one.

```
pipx run kedro new
# answer the questions it asks
```

> I use this quite often to try out new things in a safe place.

## Make a virtual environment.

### Using Conda

Conda is a fine choice to manage your virtual environments.  It used to
make things so much easier on windows that it was almost required.
Nowadays getting python running on windows has become so much easier
that this is less so.

``` python
conda create -n my-project python=3.8 -y
conda activate my-project
python  -m pip install --upgrade pip
pip install -e src
```

> one great benefit of conda is that it lets you choose the interpreter
> to go with your virtual environment.

Your new environment will be listed in your list of conda env here.

``` python
conda info --envs
```

### Using venv

`venv` is what I use now.  Nothing against conda, it works great.
`venv` just feels a bit lighter and more common.  I've actually grown to
appreciate that the `venv` is right where I put it, most often in the
project directory.

```
python -m venv .venv
source ./.venv/bin/activate
python  -m pip install --upgrade pip
pip install -e src
```

### using pipenv

`pipenv` is another fine choice.  I like how in one command it makes the
environment and activates it for you.  `pipenv` also puts virtual
environments in the global directory.

```
pipx run pipenv shell
python  -m pip install --upgrade pip
pip install -e src
```

## Make pipelines

Now go make some pipelines with your new project, try something wild,
break it, and make another.
