---
date: 2022-05-11 07:16:34
templateKey: til
title: convert your qutebrowser config to config.py
tags:
  - python

---

When you first start qutebrowser It will create some config files in
your home directory for you, but they will be empty.

## Config

As far as I know qutebrowser will create this default config out of the
box for you, if it doesn't, then somehow it just appeared for me 😁.

``` bash
❯ tree ~/.config/qutebrowser
/home/waylon/.config/qutebrowser
├── autoconfig.yml
├── bookmarks
│   └── urls
├── config.py
├── greasemonkey
└── quickmarks

2 directories, 5 files
```

## Why convert

You might want to confvert if you are more comfortable with the python
config, or if like me you just want config in one place and you are
stealing configuration options from others who have thiers in config.py.

## Convert to py

```
```
