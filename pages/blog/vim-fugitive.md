---
templateKey: blog-post
tags: ['kedro', 'python']
title: Vim Fugitive
date: 2021-05-08T22:51:53
status: draft

---


``` vim
:G
:G status
:G commit
:G add %
:Gdiff
:G push
:Glog
```


## Add current file and commit with diff in a split

``` vim
function! s:GitAdd()
    exe "G add %"
    exe "G diff --staged"
    exe "only"
    exe "G commit"
endfunction
:command! GitAdd :call s:GitAdd()
nnoremap gic :GitAdd<CR>
```

## :on[ly]

_C-W o_

:on[ly] will make the current buffer the only one on the screen.  This is super helpful as many of fugitive commands will open in a split by default.


## C-I C-O

_cycle through the jumplist_

This one has nothing to do with fugitive, but is a native vim feature that
makes fugitive glorious.  Before I realized how to utilize `C-i` and `C-o`, I
would get completely lost when using fugitive.  Digging deep into the log,
opening a file from a specific commit, then no way to get back where I was in
the log.


> C-i jump

### :jump[s]

_show the jumplist_

> The jumplist is sorted Oldest to newest


### :Telescope jumplist

When navigating the jumplist with `:Telescope jumplist`, it will add a new entry
to the jumplist and let you get back to where you were with a `C-O`.

> :Telescope jumplist adds to the jumplist


## C-W J / C-W L

## :G log

``` bash
:G log
:G log -p
:Glog
```

## Ggrep

``` bash
:Ggrep python **/*md
```

Unlike `:vim[grep]` you don't need to specify a file glob.
``` bash
:Ggrep python
```

