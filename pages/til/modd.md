---
date: 2025-08-25 10:48:01
templateKey: til
title: modd
published: true
tags:
  - dev

---

Today I gave [modd](https://github.com/cortesi/modd) a try, and it seems like a
good file watcher executor.  I tried using libnotify to send desktop
notifications, but all I got was modd, I might not have notifications setup
right on the awesomewm machine.

config goes in `modd.conf`

``` config
**/*.py {
  # check formatting via ruff
  prep: ruff format --check .

  # check docstring formatting
  prep: pydocstyle .
  #
  # # check type hints via ty
  prep: ty check .
  #
  # # run linter via ruff
  prep: ruff check .
}
```

I installed it using installer from jpillora, pulling pre-built binaries right
out of the github repo.

``` bash
curl https://i.jpillora.com/cortesi/modd | bash
```

Then you can install it, and on file change it will run the commands you
configured.

``` bash
modd
```
