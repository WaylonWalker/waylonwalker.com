---
date: 2022-10-27 20:13:20
templateKey: til
title: nvim navic
published: true
jinja: false
tags:
  - vim

---

With the latest release of version of nvim 0.8.0 we get access to a new winbar
feature.  One thing I have long wanted somewhere in my nvim is navigation for
pairing partners or anyone watching can keep track of where I am.  As the
driver it's easy to keep track of the file/function you are in.  But when you
make big jumps in a few keystrokes it can be quite disorienting to anyone
watching, and having this feedback to look at is very helpful.

!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C6.0 -Ak_lms -S2841371882](https://stable-diffusion.waylonwalker.com/000362.2841371882.webp)

## winbar

nvim exposes the winbar api in lua, and you can send any text to the winbar as follows.

``` lua
vim.o.winbar = "here"
```

You can try it for yourself right from the nvim command line.

``` vim
:lua vim.o.winbar = "here"
```

Now you will notice one line above your file with the word `here` at the very
beginning.

## Clearing the winbar

If you want to clear it out, you can just set it to an empty string or `nil`.

``` vim
:lua vim.o.winbar = ""
:lua vim.o.winbar = nil
```

## Setting up nvim-navic

You will need to install `nvim-navic` if you want to use it.  I added it to my
plugins using Plug as follows.

``` vim
call plug#begin('~/.local/share/nvim/plugged')
Plug 'SmiteshP/nvim-navic'
call plug#end()
```

> Note! `nvim-navic` does require the use of the nvim lsp, so if you are not
> using it then maybe this won't work for you.

I created an `on_attach` function long ago, cause that's what Teej told me to
do.  Now I am glad I did, because it made this change super easy.

``` lua
local function on_attach(client, bufnr)
    if client.server_capabilities.documentSymbolProvider then
        navic.attach(client, bufnr)
    end
end
```

Then you need to use that `on_attach` function on all of the lsp's that you
want navic to work on.

Then in a lua file you need to setup the winbar, for now I put this in my
lsp-config settings file, but eventually I want to move my settings to lua and
put it there.

``` lua
vim.o.winbar = " %{%v:lua.vim.fn.expand('%F')%}  %{%v:lua.require'nvim-navic'.get_location()%}"
```

## What my winbar looks like

What I have right now is everything someone who is watching would need to know
to navigate to the same place that I am in the project.

``` text
 waylonwalker/app.py   Link >  on_click
```

![nvim-navic-example.webp](https://dropper.waylonwalker.com/api/file/d01f3307-6397-4fdf-a870-0165b331d186.webp)

## Diff

Here are the changes that I made to to my plugins list and my lsp-config to get
it.

```diff
 /home/u_walkews/.config/nvim/plugins.vim
call plug#begin('~/.local/share/nvim/plugged')
+Plug 'SmiteshP/nvim-navic'
```

``` diff
#  /home/u_walkews/.config/nvim/lua/waylonwalker/lsp-config.lua
-local function on_attach() end
+local navic = require("nvim-navic")
+local function on_attach(client, bufnr)
+    if client.server_capabilities.documentSymbolProvider then
+        navic.attach(client, bufnr)
+    end
+end
+
+vim.o.winbar = " %{%v:lua.vim.fn.expand('%F')%}  %{%v:lua.require'nvim-navic'.get_location()%}"
```

## GH commit

If you want to see the change on GitHub, here is the
[diff](https://github.com/WaylonWalker/devtainer/commit/62298a935d93a2cf21e1c965d323363bcbd22881)

[![nvim-navic-setup-gh-diff.webp](https://dropper.waylonwalker.com/api/file/5efbd396-2716-49d3-833b-3004f1726afe.webp)](https://github.com/WaylonWalker/devtainer/commit/62298a935d93a2cf21e1c965d323363bcbd22881)
