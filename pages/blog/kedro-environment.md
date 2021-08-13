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

* stores environment in a root directory i.e. `~/miniconda3`
* conda can use its own way to manage environments `environment.yml`
* the python interpreter is packaged with the environment

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

* environments are typically stored in the project directory
* does not package the interpreter

## pipenv

```
pipx run pipenv shell
python  -m pip install --upgrade pip
pip install -e src
```

* stores environment in a root directory i.e. `~/.local/share/virtualenvs/`
* pipenv can use its own way to manage environments `pipfile`
* does not package the interpreter
