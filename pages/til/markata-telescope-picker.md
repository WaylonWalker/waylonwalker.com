---
date: 2022-01-23 04:52:20.855900
templateKey: til
title: Markata Filters as Telescope Pickers in Neovim
tags:
  - python
  - cli
  - vim
  - markata
---

I often pop into my blog from neovim with the intent to look at just a
single series of posts, `til`, `gratitude`, or just see todays posts.
[Markata](https://markata.dev/) has a great way of mapping over posts
and returning their path that is designe exactly for this use case.

[Markata listing out posts from the command line](https://images.waylonwalker.com/markta-list-todays-posts.png)

To tie these into a Telescope picker you add the command as the
find_command, and comma separate the words of the command, with no
spaces.  I did also `--sort,date,--reverse` in there so that the newest
posts are closest to the cursor.

``` python
nnoremap geit <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,date==today<cr>
nnoremap geil <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,templateKey=='til',--sort,date,--reverse<cr>
nnoremap geig <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,templateKey=='gratitude',--sort,date,--reverse<cr>
```

> NOTE telescope treates each word as a string, do not wrap an extra
> layer of quotes around your words, it gets messy.

![using this picker in neovim](https://images.waylonwalker.com/markata-list-telescope-picker.png)
