---
templateKey: blog-post
tags:
  - vim
  - linux
title: I made a neovim plugin
date: 2021-10-05T08:04:44
published: true
---

I've slowly adding more and more lua functions into my neovim configuration,
and recently I noticed a pattern for a class of functions that reach out to run
shell commands that can be abstracted away.

[https://youtu.be/8m5ipBuopPU](https://youtu.be/8m5ipBuopPU){.hoverlink}

## Telegraph.nvim

Check out the project [readme](https://github.com/WaylonWalker/Telegraph.nvim)
for the most up to date details on the plugin itself.

## Motivation

I want a simple way to make remaps into shell commands that can open new tmux
windows, popups, or just run a command with context from the editor.

For example I want to make remaps to do things like open the current file in lookatme.

```vim
# vim :terminal
nnoremap <leader>s <cmd>Telegraph pipx run lookatme {filepath} --live-reload --style gruvbox-dark<cmd>

# tmux session
nnoremap <leader><leader>s <cmd>lua require'telegraph'.telegraph({cmd='pipx run lookatme {filepath} --live-reload --style gruvbox-dark', how='tmux'})<CR>

# tmux popup
nnoremap <leader><leader>S <cmd>lua require'telegraph'.telegraph({cmd='pipx run lookatme {filepath} --live-reload --style gruvbox-dark', how='tmux_popup'})<CR>
```

The main goal here is that remaps become one liners that can just be put
directly in my `init.vim` without creating a whole new lua module for each
shell command I want to bind.

## how

`telegraph` takes in a `how` argument to determine where to tun the command.j

- `term`(default) runs command in the built in terminal
- `tmux` runs command in a new tmux session and joins it.
- `tmux_popup` runs command in a tmux popup window.
- `tmux_popup_session` runs command in a tmux session and displays it in a popup
- `subprocess` runs command in a subprocess

## Format strings

The current set of format strings that can be used with telegraph. Placing
these in braces `{}` within your command will get rendered into something with
context from the editor.

- `cword` - the current word under the cursor
- `cWORD` - the current BIG Word under the cursor
- `cline` - the current line under the cursor
- `filepath` - the filepath of the current file
- `filename` - the filename of the current file
- `parent` - the parent directory of the current file
- `current_session_name` - name of the current tmux session
- `cwd` - the current working directory

## Give it a ⭐

Check out the [repo](https://github.com/WaylonWalker/Telegraph.nvim) and give
it a star if its something that interests you.
