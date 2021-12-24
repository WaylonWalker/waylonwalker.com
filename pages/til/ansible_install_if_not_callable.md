---
date: 2021-12-24T20:24:48
templateKey: til
title: Installing packages with ansible only if they do not exist
tags:
  - python
  - rich

---

Part of my neovim setup requires having the `black` python formatter
installed and callable.  I install it with `pipx` so that I don't have
to manage a virtual environment and have it available everywhere.  So
far this works well for me, if there are ever breaking changes I may
need to rethink this.

re-installing a bunch of things that are already installed can be quite
a waste and really add up to my ansible run time, so for most of my
ansible tasks that install a command like this I have been following
this pattern.

1. check if the command is installed with `command -v <command>`
2. register that step
3. ignore if that step fails
4. add a `when: <xxx>_exists is failed` condition to the step that
   installs that command.

``` yaml
- name: check is black installed
  shell: command -v black
  register: black_exists
  ignore_errors: yes

- name: install black
  when: black_exists is failed
  shell: pipx install black
```
