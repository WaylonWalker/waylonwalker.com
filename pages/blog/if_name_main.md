---
templateKey: blog-post
tags: ['python']
title: What is if __name__ == "__main___", and how do I use it.
date: 2021-05-06T09:43:17
status: draft

---

When a python module is called it is assigned the `__name__` of `__main__`
otherwise if its imported it will be assigned the `__name__` of the module.


## Concrete example

Let's create a module to play with `__name__` a bit.  We will call this module
`nodes.py`.  It is a module that we may want to run by itself or import and use
in other modules.

```python
#!python
# nodes.py

if __name__ == "nodes":
    import sys
    import __main__

    print(f"you have imported me {__name__} from {sys.modules['__main__'].__file__}")

if __name__ == "__main__":
    print("you are running me as main")
```

I have set this module up to execute one of two if statements based on whether
the module itself is being ran or if the module is being imported.  

> Note it is not common to have a `if __name__ == "nodes":` block, this is just
> for demnonstration purposes.

## running python nodes.py

Running a python script with the command `python <filename.py>` will execute
your script top to bottom.

```bash
python nodes.py
```

> This will print out `you are running me as main`

<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/if_name_main_python_nodes.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/if_name_main_python_nodes.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

https://waylonwalker.com/install-miniconda/

> If you don't already have python installed try using miniconda or replit.com

## running ./nodes.py

You can also simply execute the script from bash if you first set the module to
be executable.

```
chmod +x nodes.py
./nodes.py
```

<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/if_name_main_nodes.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/if_name_main_nodes.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

> Note once you have set the file to be executable, it will remain executable
> `chmod +x nodes.py` is only needed one time, even if you edit the file.

## pipeline.py

Let's create a second module `pipeline.py` and import the first module `nodes` and see what happens.

``` python
#!python
# pipeline.py
import nodes
```

Just like nodes we can can run pipeline either way if its executable

```bash
python pipeline.py
# must run chmod +x pipeline.py first.
./pipeline.py
```

> Either way it will print out `you have imported me nodes from ./pipeline.py`

<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/if_name_main_pipeline.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/if_name_main_pipeline.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

## REPL

If we were to `import nodes` from the repl we would see an error in this case,
due to the fact that there is no `__main__` file since its a repl session.

## Use Cases

The main use case for `if __name__ == "__main__":` is flexibility.  Simply
importing a module should not execute any code, print anything to the screen,
change your filesystem, or generally have any side effects in most cases. It is
something that most python users would not expect.  We can use this block to
make it such that the module can be both imported and executed.

### rich

The [rich](https://github.com/willmcgugan/rich) library uses it to make
examples of each module print to the screen if its executed.  I personally
think this is a fantastic idea.

<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/if_name_main_rich.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/if_name_main_rich.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
<

### etl

In my world of data analysis we often setup a script of functions that will
behave as an etl pipeline of sorts.  Since we may want to reuse some of these
functions in other scripts its common to hide the actual execution of these
functions in a `if __name__ == "__main__":` block so that we don't start making
changes to the data simply by importing the module.

### cli

Most cli applications will leverage `if __name__ == "__main__":` to run
something when called as a script instead of being imported. This allows us do
do things such as testing much easier.

> Check out the example on the first page of the
> [click](https://click.palletsprojects.com/en/7.x/) framework's docs

## Recap

`if __name__ == "__main__":` is not so cryptic or scary, its just looking to
see if this module was called as a script or imported from somewhere else, and
executing some different behavior based on how it was called.

```
if __name__ == "__main__":
    print("you are running me as main")
```
