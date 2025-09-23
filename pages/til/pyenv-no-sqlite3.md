---
date: 2022-05-31 14:18:52
templateKey: til
title: pyenv no module named '_sqlite3'
tags:
  - python

---

I've been trying to adopt pyenv for a few months, but have been completely
blocked by this issue on one of the main machines I use.  Whenever I start up
ipython I get the following error.

```
ImportError: No module named '_sqlite3
```

I talked about why and how to use pyenv along with my first impressions in
[this post](/til/pyenv-first-impressions)

## pyenv/issues/678

According to [#678](https://github.com/pyenv/pyenv/issues/678) I need to
install `libsqlite3-dev` on ubuntu to resolve this issue.

## install libsqlite3-dev

`libsqlite3-dev` can be installed using apt

```bash
sudo apt install libsqlite3-dev
```

## But wait....

When I make a fresh env and install ipython I still get the same error and I am
still not able to use ipython with pyenv.

```python
ImportError: No module named '_sqlite3
```

## re-install python

After having this issue for awhile an coming back to
[#678](https://github.com/pyenv/pyenv/issues/678) several times I realized that
`libsqlite3-dev` needs to be installed while during install.

```bash
pyenv install 3.8.13
```

I think I had tried this several times, but was missing the `-y` option each
time.  You gotta read errors like this, I am really good at glossing over them.

![pyenv-install-exists.webp](https://dropper.wayl.one/api/file/017121e2-1f51-4910-bfce-86813a7f90a3.webp)

## Let's never have this issue again.

When you spend months living with little errors like this and finally fix it,
its good to make sure that it never happens again.  Whenever I start a new
ubuntu machine I run an ansible playbook that does all the setup for me.  I
added `libsqlite3-dev` to my core install in
[64c85ca](https://github.com/WaylonWalker/devtainer/commit/64c85ca1b38eefe95dfc8723c1e83e8e334cf4dc)
now it will be on all of my machines and not break again.
