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

## C-I C-O

## C-W J / C-W L
