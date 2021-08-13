---
templateKey: blog-post
tags: ['kedro', 'python']
title: kedro-environment
status: draft

---

## conda

I prefer to use conda as my virtual environment manager of choice as it give me
both the interpreter and the packages I install.  I don't have to rely on the
system version of python or another tool to maintain python versions at all, I
get everything in one tool.

``` python
conda create -n my-project python=3.8 -y
conda activate my-project
python  -m pip install --upgrade pip
pip install -e src
```

``` python
conda info --envs
```

## virtualenv

```
python -m venv .venv
source ./.venv/bin/activate
python  -m pip install --upgrade pip
pip install -e src
```

## pipenv

```
pipx run pipenv shell
python  -m pip install --upgrade pip
pip install -e src
```
