---
date: 2023-12-28 10:04:57
templateKey: til
title: nvim stupid gf bind
published: true
tags:
  - vim
jinja: false

---

So after months of fighting with gf not going to template files, I finally
decided to put in some effort to make it work.

> This was the dumbest keybind in my config, that I copied from someone else
> without understanding it.

## What I am trying to do

I have jinja templates in a directory called `templates`.  I want to bind gf to
open a template file, but it is trying to open a new file `./base.html`

``` html
{% extends "base.html" %}
{% if request.state.user %}
    {% block title %}Fokais - {{ request.state.user.full_name }} {% endblock %}
{% else %}
    {% block title %}Fokais {% endblock %}
{% endif %}
{% block content %}
    {% if request.state.user %}
        <h1 id="title"
            class="inline-block mx-auto text-5xl font-black leading-loose
            text-transparent bg-clip-text bg-gradient-to-r from-red-600
            via-pink-500 to-yellow-400 ring-red-500 text-shadow-xl
            text-shadow-zinc-950 ring-5">
            {{ request.state.user.full_name }}
        </h1>
    {% endif %}
    {% include "me_partial.html" %}
{% endblock %}
```

## What did not work

I tried all sorts of changes to my path, but it still didn't work.

``` lua
vim.api.nvim_command("set path+=templates/**")

```

## What I found

after digging into my keymap I found that I had remaped `gf` to `edit` years
ago.  This works great if the file is in your current directory, and if it's not
it makes the file.  This bind completely breaks vim's ability to `:find` files
and was a terrible keybind that I added probably from someone else years ago
and have literally never used this feature.  If `gf` opens an empty file I
always close it and assume that vim failed to `:find` the file.

``` lua
-- Allow gf to open non-existent files
set("", "gf", ":edit <cfile><CR>")
```

## Yes, after that fix I still needed to adjust my path

I ended up with the following in my options.lua.

``` lua
-- look for jinja templates in the templates directory
vim.opt.path:append("templates/**")
```
