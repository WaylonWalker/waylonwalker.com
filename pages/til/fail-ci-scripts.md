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
command failure.  Otherwise each line will set the exit status, but only the
last one will be passed to ci.

``` bash
#!/bin/bash -e
```

## What is -e

The -e flag to the bash command allows your script to exit immediately if any
command within the script returns a non-zero exit status. This can be useful
for ensuring that your script exits with an error if any of the commands it
runs fail, which can help you identify and debug issues in your script. For
example, if you have a script that runs several commands and one of those
commands fails, the script will continue running without the -e flag, but will
exit immediately if the -e flag is present. This can make it easier to
troubleshoot your script and ensure that it runs correctly.

## Solution for Windows

In windows the solution is not quite as simple.  You can define a function in a
Windows batch script that wraps an if statement to check the exit status of a
command and handle any errors that may have occurred. Here is an example of how
you might define a function called "check_error" that does this:

``` cmd
:check_error
if errorlevel 1 (
  echo An error occurred!
  exit /b 1
)
```

To use this function in your script, you would simply call it after running a
command, like this:

``` cmd
some_command
call :check_error
```

This would run the "some_command" and then call the "check_error" function to
check the exit status and handle any errors that may have occurred. This
approach allows you to reuse the error-checking logic in your script, which can
make it easier to write and maintain.
