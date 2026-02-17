---
title: '💭 nvim: `vim.o.cmdheight=0`'
date: 2023-12-14T14:20:17
templateKey: link
link: https://vi.stackexchange.com/questions/39947/nvim-vim-o-cmdheight-0-looses-the-recording-a-macro-messages
tags:
  - nvim
published: true

---

> I fixed my missing macro recording indicator that I lost and was never quite sure why. (because I forgot that I set cmdheight=0).

``` lua
vim.cmd [[ autocmd RecordingEnter * set cmdheight=1 ]]
vim.cmd [[ autocmd RecordingLeave * set cmdheight=0 ]]
```

[Original thought](https://vi.stackexchange.com/questions/39947/nvim-vim-o-cmdheight-0-looses-the-recording-a-macro-messages)
