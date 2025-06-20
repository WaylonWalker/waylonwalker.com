---
date: 2022-01-03T12:37:32
templateKey: til
title: copier template variables
tags:
  - python
  - bash
  - copier

---

I've been looking for a templating tool for awhile that works well with
single files.  My go to templating tool `cookiecutter` does not work for
single files, it needs to put files into a directory underneath of it.

## template variables

By default copier uses double square brackets for its variables.
variables in files, directory_names, or file_names will be substituted
for their value once you render them.

``` python
# hello-py/hello.py.tmpl
print('hello-[[name]]')
```

> note! by default copier will not inject variables into your
> `template-strings` unless you use a .tmpl suffix.

Before running copier we need to tell copier what variables to ask for,
we do this with a copier.yml file.

``` yaml
# copier.yml
name:
  default: my_name
  type: str
  help: What is your name
```

## installing copier

I prefer to install cli tools that I need globally with pipx, this
always gives me access to the tool without worrying about dependency
conflicts, bloating my system site-packages, or managing a separate
virtual environment for it myself.

``` bash
pipx install copier
```

## running copier

When running `copier copy` we pass in the directory of the template, and
the directory that we want to render the template into.

``` bash
copier copy hello-py .
```

> note! the directory '.' is often referred to in cli programs to
> represent the current working directory that we are calling the
> command from.

## results

The resulting files will have your variables injected into them if you have
setup your template and copier.yml up correctly.

``` python
print('hello-you')
```
