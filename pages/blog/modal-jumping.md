---
templateKey: blog-post
tags: ['vim', ]
title: Modal jumping
date: 2021-06-03T21:30:35
status: draft

---

```
nnoremap <leader>e :execute getline(".")<cr>j
```

```
nnoremap <c-j> g,
nnoremap <c-k> g;
```

```
nnoremap <c-j> <c-]>
nnoremap <c-k> g;
```

```
nnoremap <c-j> :cnext<cr>
nnoremap <c-k> :cprev<cr>
```

```
nnoremap <c-j> :lnext<cr>
nnoremap <c-k> :lprev<cr>
```

```
nnoremap <c-j> :tnext<cr>
nnoremap <c-k> :tprevious<cr>
nnoremap <c-j> :trewind<cr>
nnoremap <c-k> :tprevious<cr>
```

