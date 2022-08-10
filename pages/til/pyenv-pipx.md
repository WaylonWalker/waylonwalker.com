---
date: 2022-08-09 20:38:42
templateKey: blog-post
title: Using Different versions of python with pipx | pyenv
status: 'draft'
tags:
  - python

---

I love using pipx for automatic virtual environment management of my globally
installed python cli applications, but sometimes the application is not
compatible with your globally installed `pipx`

## Which version of python is `pipx` using??

This one was not  obvious to me at first, please let me know if there is a
better way.  I am pretty certain that this is not the ideal way, but it works.

My first technique was to make a package that printed out `sys.version`.

``` bash
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

```
export PIP_REQUIRE_VIRTUALENV=true
```

```
pyenv global 3.10.5
pip install pipx
pipx run --spec git+https://github.com/waylonwalker/pyvers pyvers

3.10.5 (main, Jun  6 2022, 18:49:26) [GCC 12.1.0]
```

```
pyenv global 3.8.13
pip install pipx
pipx run --spec git+https://github.com/waylonwalker/pyvers pyvers

3.8.13 (default, Aug  8 2022, 21:06:56)
[GCC 12.1.0]
```
