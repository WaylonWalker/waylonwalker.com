---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['bash', 'linux']
title: Creating Reusable Bash Scripts
date: 2020-08-13T05:00:00Z
status: published
description: Bash is a language that is quite useful for automation no matter
    what language you write in. Bash can do so many powerful system-level tasks.
    Even if you are on windows these days you are likely to come across bash
    inside a cloud VM, Continuous Integration, or even inside of docker.
cover: '/static/reusable-bash.png'

---

Bash is a language that is quite useful for automation no matter what language you write in. Bash can do so many powerful system-level tasks. Even if you are on windows these days you are likely to come across bash inside a cloud VM, Continuous Integration, or even inside of docker.

I have three techniques that help me write more composable bash scripts.

1. [functions](#functions)
  * [Arguments](#arguments)
  * [positional arguments](#positional-arguments)
  * [All Arguments](#all-arguments)
1. [Error Handling](#error-handling)
1. [main script](#main-script)

---

## Functions
_Break scripts down into reusable components_

Functions in bash are quite simple. They are something that I wish I would have started using long ago. They make your code much more reusable. I often use them in my aliases as well since they can simplify the process and allow more flexibility.

_<small><mark>syntax</mark></small>_

``` bash
#!/bin/sh
# hello_world
hello_world () {
    echo "hello world"
}
```

Source the file to load the function and run it from the terminal.

_<small><mark>run it</mark></small>_

``` bash
source hello_world
hello_world
```

_<small><mark>outputs</mark></small>_

``` bash
hello world
```
---

## Arguments
_Make functions a little more flexible_

Arguments and options are quite a bit more complex in bash. For now, we will focus on the basics which are not all that bad.

### positional arguments
_easiest and most common to use_

Positional arguments can be pulled out quite easily using `$1` for the first one, `$2` for the second, and so on.

**note** `$0` is the command that was called. You will see this often used to find the command called to open up your current shell.

_<small><mark>syntax</mark></small>_
``` bash
#!/bin/sh
# hello
hello () {
    echo "hello $1"

```

_<small><mark>run it</mark></small>_

``` bash
source hello
hello Waylon
```

Now we have a function that accepts positional arguments and we can call it by passing things into it.

_<small><mark>outputs</mark></small>_

``` bash
hello Waylon
```

More than one argument would be ignored since we are only looking at `$1`.

_<small><mark>run it</mark></small>_

``` bash
source hello
hello Waylon Walker
```

_<small><mark>outputs</mark></small>_

``` bash
hello Waylon
```

Just the same as before since we do not use the second argument.

### All Arguments

Bash has another special variable `$@` that stores **all arguments** in one.

_<small><mark>syntax</mark></small>_

``` bash
#!/bin/sh
# hello
hello () {
    echo "hello $@"
}
```

Just the same as before.

_<small><mark>run it</mark></small>_

``` bash
source hello
hello Waylon Walker
```

Now the function will output all arguments that are passed into it since we are using the `$@` variable.

_<small><mark>outputs</mark></small>_

``` bash
hello Waylon Walker
```

---

## Error Handling
_Super powers in a single line_

The easiest and most common way to handle an error in bash is through the use of the logical operators `&&` (and) and `||` (or).

Here I have a concrete example from earlier today. I was creating a bash script to run a python script from cron. The bash script is there to make sure that we have the python environment, activate it, and run. If it doesn't have it, it should create it.

``` bash{15-19}{numberLines: true}
# creates the conda environment
create_env() {
    conda create -n "$1" python=3.8
    conda activate "$1"
    pip install -r requirements.txt
}


# checks if the conda environment exists
env_exists() {
conda info --envs | awk '{print $1}' | tail -n +3 | grep -w "$1" > /dev/null
}


# creates the conda environment if it doesn't exist
create_if () {
env_exists "$1" && echo "environment exists" || create_env "$1"
}

create_if my_env
```

If we look at the `create_if` function, it will check if the environment exists if there is a passing status code `0`, then it will run `echo "environment exists"` otherwise it will run `create_env $1`.

**note** Inside of `env_exists` grep will look for whole words if there is a match it will give a status code 0 if it finds a match and not 0 if there is no match.

---

## main script

\_`if __name__ == " __main__"`\_

The last thing I want to discuss is making a bash script both runnable and sourceable. This makes it so that you can `source filename.sh` and run each function individually, or `bash filename.sh` to run the script. This is a similar concept to `if __name__ == " __main__"` from python.

I did try this from bash and zsh with success. The following is an example that would pass all arguments into a main function.

_<small><mark>syntax</mark></small>_

``` bash
if [["${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```

Extending the example above that created a python example if necessary we can create the env if necessary, activate the environment, and run the script.

_<small><mark>syntax</mark></small>_

``` bash
if [["${BASH_SOURCE[0]}" == "${0}" ]]; then
create_if my_env
conda activate my_env
python script.py
fi
```

Using this syntax to run our "main" functions will allow us to both runs the script or source the script to utilize the functions that we created.
