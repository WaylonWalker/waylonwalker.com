---
title: '💭 pipedream/justfile at main · thechangelog/pipedream'
date: 2024-12-14T16:54:34
template: link
link: https://github.com/thechangelog/pipedream/blob/main/justfile
tags:
  - bash
  - linux
  - just
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/thechangelog/pipedream/blob/main/justfile]]

I found this nugget in thechangelogs justfile, it lets you add color to your justfile with variables quite easily.

``` bash
# https://linux.101hacks.com/ps1-examples/prompt-color-using-tput/

_BOLD := "$(tput bold)"
_RESET := "$(tput sgr0)"
_BLACK := "$(tput bold)$(tput setaf 0)"
_RED := "$(tput bold)$(tput setaf 1)"
_GREEN := "$(tput bold)$(tput setaf 2)"
_YELLOW := "$(tput bold)$(tput setaf 3)"
_BLUE := "$(tput bold)$(tput setaf 4)"
_MAGENTA := "$(tput bold)$(tput setaf 5)"
_CYAN := "$(tput bold)$(tput setaf 6)"
_WHITE := "$(tput bold)$(tput setaf 7)"
_BLACKB := "$(tput bold)$(tput setab 0)"
_REDB := "$(tput setab 1)$(tput setaf 0)"
_GREENB := "$(tput setab 2)$(tput setaf 0)"
_YELLOWB := "$(tput setab 3)$(tput setaf 0)"
_BLUEB := "$(tput setab 4)$(tput setaf 0)"
_MAGENTAB := "$(tput setab 5)$(tput setaf 0)"
_CYANB := "$(tput setab 6)$(tput setaf 0)"
_WHITEB := "$(tput setab 7)$(tput setaf 0)"
``` 

Usage
``` bash
echo:
    echo {{_BOLD}}{{_GREEN}}hello there{{_RESET}}
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
