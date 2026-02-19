---
title: '💭 nvim: `vim.o.cmdheight=0`'
date: 2023-12-14T14:20:17
template: link
link: https://vi.stackexchange.com/questions/39947/nvim-vim-o-cmdheight-0-looses-the-recording-a-macro-messages
tags:
  - nvim
  - thoughts
  - thought
  - link
published: true

---

![[https://vi.stackexchange.com/questions/39947/nvim-vim-o-cmdheight-0-looses-the-recording-a-macro-messages]]

I fixed my missing macro recording indicator that I lost and was never quite sure why. (because I forgot that I set cmdheight=0).

``` lua
vim.cmd [[ autocmd RecordingEnter * set cmdheight=1 ]]
vim.cmd [[ autocmd RecordingLeave * set cmdheight=0 ]]
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
