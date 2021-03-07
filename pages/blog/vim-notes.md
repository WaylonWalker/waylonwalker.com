---
templateKey: 'blog-post'
title: Vim Notes
date: 2018-02-01
status: Draft
description: none
cover: "./flex.png"
---

# vim notes

## Using c to change text

I have gone quite awhile without using ```c``` and instead using ```d```.  The reason that I started using ```c``` is because it automatically places you into insert mode.  This not only saves me one keystroke for commands such as ```diwi``` is now ```ciw```, but it also works with the repeat ```.``` command!!!  This is huge.  When refactoring a document I had been creating a macro to change one word to another, using ```c``` instead of ```d``` allows the use of the ```.``` rather than needing to create a macro.

## Case for vim

**Sublime/VSCode cannot**

* edit a macro register
* register


## autocomplete

<C-x> <C-p> repeats previously typed text

    1. Whole lines                                     |i CTRL-X CTRL-L|
    2. keywords in the current file                    |i CTRL-X CTRL-N|
    3. keywords in 'dictionary'                        |i CTRL-X CTRL-K|
    4. keywords in 'thesaurus', thesaurus-style        |i CTRL-X CTRL-T|
    5. keywords in the current and included files      |i CTRL-X CTRL-I|
    6. tags                                            |i CTRL-X CTRL-]|
    7. file names                                      |i CTRL-X CTRL-F|
    8. definitions or macros                           |i CTRL-X CTRL-D|
    9. Vim command-line                                |i CTRL-X CTRL-V|
    10. User defined completion                        |i CTRL-X CTRL-U|
    11. omni completion                                |i CTRL-X CTRL-O|
    12. Spelling suggestions                           |i CTRL-X s|
    13. keywords in 'complete'                         |i CTRL-N|

## z-commands

```zn```		Fold none: reset 'foldenable'.  All folds will be open.
