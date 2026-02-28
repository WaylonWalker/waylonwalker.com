---
title: '💭 Background Image | Wallpaper · Issue #3059 · helix-editor/helix'
date: 2024-10-08T13:02:53
template: link
link: https://github.com/helix-editor/helix/issues/3059
tags:
  - helix
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/helix-editor/helix/issues/3059]]

How to make helix themes transparent.  You can make any built-in theme transparent in helix with one line, a few extras and you can make all the pop ups, help menus and status line trransparant as well.

``` bash
mkdir -p ~/.config/helix/themes
hx
```

`:o ~/.config/helix/themes/dracula_transparant.toml`

``` toml
# ~/.config/helix/themes/dracula_transparant.toml
inherits = "dracula"
"ui.background" = { fg = "foreground" }
"ui.menu" = { fg = "white" }
"ui.popup" = { fg = "white" }
"ui.window" = { fg = "white" }
"ui.help" = { fg = "light-gray" }

"ui.statusline" = { fg = "gray" }
"ui.statusline.inactive" = { fg = "black" }
```

`:config-edit`

``` toml
# ~/.config/helix/config.toml
theme="dracula_transparant"
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
