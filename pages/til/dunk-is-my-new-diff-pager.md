---
date: 2022-04-04 15:47:00.613220
templateKey: til
title: Dunk is my new diff pager
tags:
  - python
  - linux
  - python

---

[Dunk](https://github.com/darrenburns/dunk) is a beautiful git diff tool
built on top of [rich](https://github.com/Textualize/rich).

Browsing through twitter the other day I discovered it through this
tweet by [_darrenburns](https://twitter.com/_darrenburns).

https://twitter.com/_darrenburns/status/1510350016623394817

## try it

You can try it with pipx.

```bash
git diff | pipx run dunk
```

## install it

If you like it, you can install it with pip or pipx, I prefer pipx for
cli applications like this.


```bash
pipx install dunk
```

## set it as your default pager

You can configure dunk as your default pager with the command line, or
by editing your `.gitconfig` file.

```bash
git config --global pager.diff dunk
```

```toml
[pager]
    diff = dunk

```

## reset it if you don't like it

You can `--unset` your pager configuration from the command line or edit
your `.gitconfig` file by hand to remove the lines shown above.

```bash
git config --global --unset pager.diff
```

## Comparison

I have some edits to a game my son and I are working on unstaged so I
ran `git diff` on that project with and without dunk to compare the
differences.

![default diff](https://imgaes.waylonwalker.com/git-diff-creeper-adventure-default.png)

Dunk just looks so good.

![dunk diff](https://images.waylonwalker.com/git-diff-creeper-adventure-dunk.png)

## Always install

If you follow along here often you know that I am a big fan of
installing all my tools in an ansible playbook so that I don't suffer
configuring a new machine for months after getting it and wondering why
its not exactly like the last.

```yaml
# Dunk - prettier git diffs
# https://github.com/darrenburns/dunk
- name: check is dunk installed
  shell: command -v black
  register: dunk_exists
  ignore_errors: yes

- name: install dunk
  when: dunk_exists is failed
  shell: pipx install dunk
```

https://waylonwalker.com/til/ansible_install_if_not_callable/

> More on conditionally installing tools with ansible in this post.
