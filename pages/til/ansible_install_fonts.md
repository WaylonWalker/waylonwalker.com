---
date: 2021-12-25T20:24:48
templateKey: til
title: Installing system nerd-fonts with ansible
tags:
  - dotfiles
  - ansible
jinja: false

---

Lately I've been on a journey to really clean up my dotfiles, and I was
completely missing fonts.  I noticed jumping into a new vm I had a bunch
of broken devicons when using Telescope with the devicons plugins.

This is one of those things that can be a total pain to get right on
some systems, and it's so nice when it's just there for you pretty much
out of the box.

1. make sure your user fonts directory exists
2. chech if the font you want exists on your machine
3. download and unzip fonts into the fonts directory
4. repeat 2-3 for all the fonts you use on your system

``` yaml
- name: ensure fonts directory
  file:
    path: "{{ lookup('env', 'HOME') }}/.fonts"
    state: directory

- name: Hack exists
  shell: "ls {{ lookup('env', 'HOME') }}/.fonts/Hack*Nerd*Font*Complete*"
  register: hack_exists
  ignore_errors: yes

- name: Download Hack
  when: hack_exists is failed
  ansible.builtin.unarchive:
    src: https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip
    dest: "{{ lookup('env', 'HOME') }}/.fonts/"
    remote_src: yes

```

https://www.youtube.com/watch?v=2MEmsinxRK4

> I made a YT based on this post

## Links

* ansible docs for [builtin.unarchive](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html)

https://waylonwalker.com/setup-yamlls/

> check out how I install yamlls using ansible
