---
templateKey: blog-post
tags: ['vim']
title: Save Vim Macro
date: 2021-01-04T00:00:00
status: published
description: ''
cover: "/static/save-vim-macro.png"

---


If you are like me, you have created a macro or two that is pure glory, and you forget how you made it after a day or so, or you immediately want to store it away as a custom keybinding. As with most things with vim, it's easy to do once you understand it.

## Creating a Macro

One of the earliest things we all learn to do in vim is to create macros, custom sets of functionality stored in a register that can be replayed later.

To create a macro, get into normal mode, then type `q` followed by a letter that you want to store the macro under.

``` vim
qq
```

> Note: a common throw-away macro register is q because it's easy to hit qq from normal mode to start recording.

## Replaying a Macro

Macros can be replayed using `@` followed by the letter that you stored the macro under.

``` vim
@q
```

## Registers

Registers are nothing more than a single character key mapping to a value of some text. As you `yank`, `delete`, or create macros in vim, it automatically stores text into these registers.

When you hit `p` paste it's simply pasting in the default register. You can also paste in any other register by hitting `"qp` where q is the register that you want to paste in.

## Listing Registers

To see what you have stored in each register, use the `:reg` command. This is a powerful tool that I have underutilized for a long time. It is really great to see what you have in each register.

``` vim
:reg
```

## making a macro into a shortcut

_a little <c-r> magic</c-r>_

The magical shortcut that makes it easy is that control + r `<C-R>` followed by a register will paste that register wherever you currently are, including the command mode.

``` vim
:nnoremap {binding} <C-R>{register}
```

## Editing a Macro

_relieve some of that Macro Pressure_

Now that we understand that macros are simply strings of text placed into a register, it becomes a bit more intuitive to edit them after being created.

First, paste the contents of the register into your current working buffer.

``` vim
<C-R>q
```

Then edit the macro and add it back to that buffer and delete it.

``` vim
"qdd
```

If your macro had multiple lines in it, you might need to.

``` vim
"qdj
"qd2j
```

## Make it recursive

One use case of editing a macro may be making it recursive after trying it out a few times. Macros can become recursive by simply calling themselves after running.

Paste in the macro.

``` vim
<C-R>q
```

Go to the end of the line and add `@q` to get called again.

``` vim
A @q
```

Replace the `q` register with the updated macro.

``` vim
"qd
```

> Note: don't use this in a shortcut as the macro may change. If you want to call the keybinding again, you will have to use noremap instead of nnoremap, but be careful as recursive remaps can be dangerous.

## Recap

``` vim
" record a macro
q{register}

" play a macro
@{register}

" list registers
:reg

" map a macro to a keyboard shortcut
:nnoremap {binding} <C-R>{register}

" edit a macro
<C-R>{register}
"{register}dd

" make a macro recursive
<C-R>{register}A@q<esc>"{register}dd
```

