---
templateKey: blog-post
tags: ["vim"]
title: Vim Replace Visual Star
date: 2021-01-10T00:00:00
status: published

---

Replacing text based on whats in the current search register is a quite handy
tool that I use often.  I believe I picked this tip up from Nick Janetakis,
check out his YouTube channel for some amazing vim tips.

https://www.youtube.com/watch?v=fP_ckZ30gbs

If there is one thing that I Like most about vim it's the ability to hack on it
and make it work well for you.

## Replacing text in vim

Vim can often be a bit verbose, but that's ok because we can hack on it, and 
make our own shortcuts and keybindings.  For instance, finding and replacing 
text requires using a command at the vim command-line `:`.  Replacing foo with
bar looks like this `:%s/foo/bar/g`, the final g means all of the foos, not just 
the first one on the line.

## making it better

I have a keybinding in my `init.vim` that will allow me to search for a pattern
with the usual `/` character, page through them as normal with `n` and `N`, but
when I press `<C-R>` it will populate the replace command for me so that all I
need to do is type out the new text.

``` vim
nnoremap <c-r> :%s/<C-R>///g<Left><Left>
```

## Note on the `<C-R>/`

In command mode `:` vim allows you to paste any text from any register into the
current command.  The `<C-R>/` will paste the text from the current search
register into the command.

`<C-R>` in command mode can paste text from any register, you can see what
registers are in use with the `:reg` command.  There are a lot of them and many
get populated automatically as you yank text or create macros.

https://waylonwalker.com/save-vim-macro

> Also see how to use <C-R> to save macros to key bindings easily
