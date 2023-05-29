---
date: 2022-08-09 20:38:42
templateKey: blog-post
title: Using Different versions of python with pipx | pyenv
status: published
tags:
  - python
---

I love using pipx for automatic virtual environment management of my globally
installed python cli applications, but sometimes the application is not
compatible with your globally installed `pipx`

## Which version of python is `pipx` using??

This one was not obvious to me at first, please let me know if there is a
better way. I am pretty certain that this is not the ideal way, but it works.

My first technique was to make a package that printed out `sys.version`.

```bash
# what version of python does the global pipx use?
pipx run --spec git+https://github.com/waylonwalker/pyvers pyvers

# what version of python does the local pipx use?
python -m pipx run --spec git+https://github.com/waylonwalker/pyvers pyvers
```

## Let's setup some other versions of python with pyenv

> If you don't already have [pyenv](https://github.com/pyenv/pyenv) installed,
> you can follow their [install
> instructions](https://github.com/pyenv/pyenv#installation) to get it.

```bash
pyenv install 3.8.13
pyenv install 3.10.5
```

## I usually require a virtual environment

I set the `PIP_REQUIRE_VIRTUALENV` environment variable to `true` to ensure
that the virtual environment is activated when pip installing, this makes it so
that I can't accidentally use the global env, which is typically not what I
want to do.

```bash
export PIP_REQUIRE_VIRTUALENV=true
# for windows users
set PIP_REQUIRE_VIRTUALENV=true
```

> This goes right into my shell startup script `~/.bashrc` or `~/.zshrc`.

## Exceptions happen

This is my one exception. I've had better luck just putting pipx right in the
global python environment. Not the system python, but each python version that
I install with pyenv.

```bash
export PIP_REQUIRE_VIRTUALENV=false
# for windows users
set PIP_REQUIRE_VIRTUALENV=false
```

## Let's install pipx

First up is python 3.10.5

```bash
pyenv global 3.10.5
pip install pipx
pipx run --spec git+https://github.com/waylonwalker/pyvers pyvers

3.10.5 (main, Jun  6 2022, 18:49:26) [GCC 12.1.0]
```

Next is python 3.8.13j

```bash
pyenv global 3.8.13
pip install pipx
pipx run --spec git+https://github.com/waylonwalker/pyvers pyvers

3.8.13 (default, Aug  8 2022, 21:06:56)
[GCC 12.1.0]
```

Now once I clost this shell I will always end up with
`PYTHON_REQUIRE_VIRTUALENV=true`, since it's in my shell startup script. So
make sure that you reset it or kill this shell before doing any damage.
