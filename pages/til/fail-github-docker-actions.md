---
date: 2022-12-07 13:09:37
templateKey: til
title: dash e your github docker actions
status: 'published'
tags:
  - bash
  - github
  - actions

---

Give github actions the -e flag in the shebang `#!` so they fail on any one
command failure.

``` bash
#!/bin/bash -e
```

The -e flag to the bash command allows your script to exit immediately if any
command within the script returns a non-zero exit status. This can be useful
for ensuring that your script exits with an error if any of the commands it
runs fail, which can help you identify and debug issues in your script. For
example, if you have a script that runs several commands and one of those
commands fails, the script will continue running without the -e flag, but will
exit immediately if the -e flag is present. This can make it easier to
troubleshoot your script and ensure that it runs correctly.
