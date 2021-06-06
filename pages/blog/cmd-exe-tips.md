---
templateKey: blog-post
tags: []
title: cmd.exe tips
date: 2020-01-23T15:18:45.000+00:00
status: published
description: cmd.exe tips

---

I spend a lot of my time at the terminal for my daily work, mostly in Linux or wsl.  One big reason for using wsl over cmd.exe is the ease of walking through history that fzf provides.  This week we had a windows bug in a cli and I was stuck in vanilla cmd.exe 😭

## > Cmder

![](https://images.waylonwalker.com/main.png)

First off if you are stuck using cmd.exe, do yourself a favor and get cmder.  It makes life just a bit easier.  It is super confugurable and comes with several power ups that make it a bit more enjoyable than cmd.exe.

## History

**F7** - Scroll through history

**F8** - Search history based

## Example

![](https://images.waylonwalker.com/cmd_exe_history_2.gif)

## .bat

The next simple technique is to save your commands into a .bat file. Any valid command ran with cmd.exe can be saved into a bat file and called again later by running it in the terminal.

**save your command**

use f7/f8 to get your command back add `> filename.bat` at the end, hit the home key and add echo to the front.  **Do not** wrap with quotes.  This is not bash.

``` bash
echo python cmd_example.py > cmd_example.bat
```

**>> append**

``` bash
echo python cmd_example2.py >> cmd_example.bat
```

## type not cat

To ensure that you got the command right... and didn't forget that you were in cmd.exe instead of bash and add quotes. you will want to see the file contents. For this reach for **type** not **cat**.

``` bash
type cmd_example.bat
```

**results**
``` bash
python cmd_example.py
python cmd_example2.py
```

## Your quick tips

let me know what quick cmd.exe tips you have.

[![tweet your tip](https://images.waylonwalker.com/2020-01-27 06-32-34_Microsoft Text Input Application.png "tweet your tip")](https://twitter.com/intent/tweet?text=@waylonwalker%20my%20favorite%20cmd.exe%20tip%20is%20...%20https%3A//waylonwalker.com/blog/cmd-exe-tips/ "tweet your tip")
