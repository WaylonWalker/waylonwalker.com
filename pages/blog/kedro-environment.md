---
templateKey: blog-post
tags: ["kedro", "python"]
title: kedro Virtual Environment
date: 2021-08-23T20:40:45
published: true
---

Avoid serious version conflict issues, and use a virtual environment anytime
you are running python, here are three ways you can setup a kedro virtual
environment.

[https://youtu.be/ZSxc5VVCBhM](https://youtu.be/ZSxc5VVCBhM){.hoverlink}

- conda
- venv
- pipenv

## conda

I prefer to use conda as my virtual environment manager of choice as it give me
both the interpreter and the packages I install. I don't have to rely on the
system version of python or another tool to maintain python versions at all, I
get everything in one tool.

```python
conda create -n my-project python=3.8 -y
conda activate my-project
python  -m pip install --upgrade pip
pip install -e src
```

```python
conda info --envs
```

- stores environment in a root directory i.e. `~/miniconda3`
- conda can use its own way to manage environments `environment.yml`
- the python interpreter is packaged with the environment

## virtualenv

Virtual env (venv) is another very respectable option that is built right into
python, and requires no additional installs or using a different distribution
of pytyhon.

```
python -m venv .venv
source ./.venv/bin/activate
python  -m pip install --upgrade pip
pip install -e src
```

- environments are typically stored in the project directory
- does not package the interpreter

## pipenv

Pipenv is another virtual enviroment tool that comes with its own system for
managing dependencies using a `pipfile`. It's main benefit is that it creates
a lockfile that will allow users to replicate the exact version of all their
packages. The typical `requirements.txt` workflow can easily break as new
version of dependecies are released between testing and deplpoyment.

```
pipx run pipenv shell
python  -m pip install --upgrade pip
pip install -e src
```

- stores environment in a root directory i.e. `~/.local/share/virtualenvs/`
- pipenv can use its own way to manage environments `pipfile`
- does not package the interpreter
