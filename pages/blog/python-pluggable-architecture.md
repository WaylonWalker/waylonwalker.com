---
templateKey: blog-post
tags: ['python']
title: 🐍 Pluggable Architecture with Python
date: 2021-01-23T00:00:00
status: draft

---

pytest has open sourced their amazing plugin framework `pluggy`, it allows
library authors to give their users a way to modify the libaries behavior
without needing to submit a change that may not make sense to the entire
library.

## Previous Experience

My experience so far as a plugin user, and plugin author has been great.
Building and using plugins are incredibly intuitive.  I wanted to dive a bit
deeper and see how they are implemented inside of a library and its a bit of a
mind bend the first time you try to do it.

## Plugins vs. Hooks

A hook is a single function that has a specific place that it is ran by the PluginManager.

A Plugin is a collection of one or more hooks.

## Layers

* library author
* plugin author
* end user

## Using a plugin

For a plugin to be registered is must be registered by the PluginManager which
is implemented by the library author.  It is the job of the library author to
determine what plugins are actively registered or disabled.  There are two
common ways that I have seen that plugins are registered, through entrypoints
or configuration.

## Using a plugin - entrypoints

Plugins that are implemented with entrypoints are the simplest for the user.
They are simply activated by `pip install plugin` or deactivated by `pip
uninstall plugin`.  The library author will show an entrypoint in their docs
which tells plugin authors how to setup entrypoints so that they will be loaded
autommatically.

## Using a plugin - config

Another way to configure plugins is through configuration.  This may come in
the form of a list in a python module or listed in a text file in the config.
This route requires the user to add the plugin to a list or import it into a
python module.

## Examples

I really stuggled to find a good example of pluggy to get started.  I found the
best way for me to understand was to create one myself.  the pluggy repo has
one simple
[example](https://github.com/pytest-dev/pluggy/blob/master/docs/examples/toy-example.py),
but it is unclear who owns each piece from the example.  The whole point of
pluggy is to pass ownership of  implementation from the library author to the
plugin author.

## Floris Bruynooghe

https://www.youtube.com/watch?v=zZsNPDfOoHU

Floris Bruynooghe has a great talk from [EuroPython
2015](https://www.youtube.com/watch?v=zZsNPDfOoHU) where he shows how to build
a project thats plugins all the way down.  His [slides](http://devork.be/talks/pluggy) are also available.

## Kedro

Kedro is a data pipelining framekwork that includes a hooks based architecture
that allows users to modify the behavior of the framework at different points
through the lifecycle.  There is a
[hooks](https://github.com/quantumblacklabs/kedro/tree/dc1ee8e06b255d4d5a4348ad8a2e78048c547279/kedro/framework/hooks)
module that implements everything, and a
[test_plugin](https://github.com/quantumblacklabs/kedro/blob/dc1ee8e06b255d4d5a4348ad8a2e78048c547279/features/steps/test_plugin/plugin.py)
that is used for testing, but also serves as a good example.

## palantir/python-language-server

Another example is the palantir python language server.  Check out their
[hookspec](https://github.com/palantir/python-language-server/blob/91a13687dbd5247374253b245124befb8d9c60c9/pyls/hookspecs.py)
module.


## Tutorial


## Plugin Components

* project_name
    * implemented by the library author
    * gives a namespace for pluggy to store hooks
* hookspec
    * created and used by libary author
* hookimpl
    * created by libary author
    * used by plugin author
* PluginManager
    * implementation of plugins in the library

## hookspec

_empty hooks created by the library author 


``` python
# hookspec.py
import pluggy

hookspec = pluggy.HookspecMarker("printer")

class PrinterHooks:
    @hookspec
    def pre_print(msg):
        "pre print hook"
        pass

    @hookspec
    def post_print(msg):
        "pre print hook"
        pass
```


## hookimpl
_used by the plugin author_

Implementations of plugins much match the name of the spec exactly.
They can include some or all of the arguments listed in the spec,
but no others.  They can be implemented as a module with functions
that match the name of the spec or as a class with methods that
match the name of the spec.


### Class Style Plugin

``` python
# plug.py
# would be imported from the library authors hookspec
from hookspec import hookimpl


class Pre:
    @hookimpl
    def pre_print(msg):
        msg = msg.upper()
        return "BEFORE"


class Post:
    @hookimpl
    def post_print(msg):
        print(f"\033[A\033[2Knot today")
```

### Module Style Plugin

``` python
# plug/Pre.py
from hookspec import hookimpl


@hookimpl
def pre_print(msg):
    msg = msg.upper()


# plug/Post.py
class Post:
    @hookimpl
    def post_print(msg):
        print(f"\033[A\033[2Knot today")
```

**note** These plugins only implement one hook.  Each plugin may
implement one or more hooks, a plugin is not required to only
implement on hook.

## Plugin Manager
_implementing the hooks into the library_

### Simple Example

``` python
import pluggy
import importlib

from hookspec import PrinterHooks
from plug import Pre

pm = pluggy.PluginManager("printer")
pm.add_hookspecs(PrinterHooks)
pm.register(Pre)

def printer(msg):
    pm.hook.pre_print(msg=msg)
    print(msg)
    pm.hook.post_print(msg=msg)
```

## Running the library

Now if we run the printer function as a user we will see this
output.

``` pycon
>>> printer('hello world')
HELLO WORLD
```

## Adding Post

Now if we register the Post plugin we will see the following output.

``` python

from plug import Pre, Post

pm.register(Pre)
pm.register(Post)
```

``` pycon
>>> printer('hello world')
not today
```

The `Post` plugin wipes away the last line from the console and
prints out `"not today"`

## Plugin Manager - with dynamic imports

In a real library we might want to allow the user to configure their
plugins through a config file.  If we do this we will need to reach
for `importlib` to handle the imports based on a string.

``` python

import pluggy
import importlib

# from hookspec import hookspec
from hookspec import PrinterHooks

# from hookspec import hookimpl

plugins = ["plug.Pre", "plug.Post"]
pm = pluggy.PluginManager("printer")
pm.add_hookspecs(PrinterHooks)

for plug in plugins:
    if isinstance(plug, str):
        # plug is a str representing a module to import
        try:
            # module style plugins
            plugin = importlib.import_module(plug)
        except ModuleNotFoundError as e:
            # class style plugins
            if "." in plug:
                mod = importlib.import_module(".".join(plug.split(".")[:-1]))
                plugin = getattr(mod, plug.split(".")[-1])
            else:
                raise e
    else:
        # plug is a module that is already imported
        plugin = plug

    pm.register(plugin)


def printer(msg):
    pm.hook.pre_print(msg=msg)
    print(msg)
    pm.hook.post_print(msg=msg)
```

## EntryPoint plugins
