---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Strip Trailing Whitespace from Git projects
date: 2020-09-30T05:00:00Z
status: published
description: 'A common linting error thrown by various linters is for trailing whitespace. I most often use flake8.  Having an automated way to fix linting errors such as trailing whitespace is invaluable.'
cover: '/static/strip-trailing-whitespace-from-git-projects.png'

---
A common linting error thrown by various linters is for trailing whitespace.  I most often use flake8.  I generally have \[pre-commit\]([https://waylonwalker.com/pre-commit-is-awesome](https://waylonwalker.com/pre-commit-is-awesome "https://waylonwalker.com/pre-commit-is-awesome")) hooks setup to strip this, but sometimes I run into situations where I jump into a project without it, and my editor lights up with errors.  A simple fix is to run this one-liner.

## One-Liner to strip whitespace

_<small><mark>bash</mark></small>_
``` bash
git grep -I --name-only -z -e '' | xargs -0 sed -i -e 's/[ \t]\+\(\r\?\)$/\1/'
```



<p style='text-align: center' align='center'>
<a href='https://waylonwalker.com/pre-commit-is-awesome'>
  <img
    style='width:400px; max-width:80%; margin: auto;'
    width='400'
    src="https://images.waylonwalker.com/pre-commit-is-awesome.png"
    alt="pre-commit article"
  />
  </a>
</p>

read more about pre-commit [here](https://waylonwalker.com/pre-commit-is-awesome).
