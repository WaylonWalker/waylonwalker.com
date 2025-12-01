---
date: 2025-09-02 13:23:21
templateKey: til
title: nvim delete current file
published: true
tags:
  - nvim

---

This one is one that I've been using quite often, I did't have a hotkey for it,
I just used the `rm` shell command.

``` vim
!!rm %<TAB><CR>
```

When you type `!!` from normal mode it will automatically put you in command
mode with `.!` pre-filled, then you just type `rm ` and `<TAB>` to
auto-complete the current file name, and `<CR>` to execute the command.

``` vim
:.!rm %<TAB><CR>

```

## Making it better

The one quirk that I don't like about this is that the buffer remains open
after deleting, and sometimes I forget to close it and end up re-creating it by
mistake when running `:wall` or `:xall`.


Create a `DeleteFile` command with vim command.

``` vim
:command! DeleteFile execute "!rm %" | bdelete!
```

Create a `DeleteFile` command with lua.
``` lua
vim.api.nvim_create_user_command(
  'DeleteFile',
  function()
    -- Delete the current file from disk
    vim.cmd('!rm %')
    -- Close the buffer without saving
    vim.cmd('bdelete!')
  end,
  {}
)
```
