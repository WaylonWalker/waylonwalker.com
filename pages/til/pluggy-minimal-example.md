---
date: 2022-01-01T20:35:27
templateKey: til
title: The most minimal pluggy example
tags:
  - python

---

Pluggy makes it so easy to allow users to modify the behavior of a framework
without thier specific feature needing to be implemented in the framework
itself.

I've really been loving the workflow of frameworks built with pluggy.  The first
one that many python devs have experience with is pytest.  I've never created a
pytest plugin, and honestly at the time I looked into how they were made was a
long time ago and it went over my head.  I use a data pipelining framework
called kedro, and have build many plugins for it.

## Making a plugin
_super easy to do_

As long as the framework document the hooks that are available and what it
passes to them it's so easy to make a plugin.  Its just importing the
`hook_impl`, making a class with a function that represents one of the hooks,
and decorating it.

``` python
from framework import hook_impl

class LowerHook:
    @hook_impl
    def start(pluggy_example):
        pluggy_example.message = pluggy_example.message.lower()
```

## installing pluggy

Installing pluggy is just like most python applications, install python, make
your virtual environment, and pip install it.

``` bash
pip install pluggy
```

## Making a plugin driven framework
_much less easy_

I have yet to find a good minimal example of how to make a pluggin system with
pluggy.  Last I read their docs, they went in deep, but missed out on a good
hello world example.

``` python
import pluggy

HOOK_NAMESPACE = "pluggy_example"
PROJECT_NAME = "pluggy_example"

hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)


class PluggyExampleSpecs:
    """
    This is where we spec out our frameworks hooks, I like to refer to them as
    the lifecycle.  Each of these functions is a hook that we are exposing to
    our users, with the kwargs that we expect to pass them.
    """
    @hook_spec
    def start(self, pluggy_example: PluggyExample) -> None:
        """
        The first hook that runs.
        """
        pass

    @hook_spec
    def stop(self, pluggy_example: PluggyExample) -> None:
        """
        The last hook that runs.
        """
        pass


class PluggyExample:
    """
    This may not need to be a class, but I wanted a container where all the
    hooks had access to the message.  This made sense to me to do as a class.
    """

    def __init__(self, message="", hooks=None) -> None:
        """
        Setup the plugin manager and register all the hooks.
        """
        self._pm = pluggy.PluginManager(PROJECT_NAME)
        self._pm.add_hookspecs(PluggyExampleSpecs)
        self.message = message
        self.hooks = hooks
        if hooks:
            self._register_hooks()

    def _register_hooks(self) -> None:
        for hook in self.hooks:
            self._pm.register(hook)

    def run(self):
        """
        Run the hooks in the documented order, and pass in any kwargs the hook
        needs access to.  Here I am storing the message within this same class.
        """
        self._pm.hook.start(pluggy_example=self)
        self._pm.hook.stop(pluggy_example=self)
        return self.message


class DefaultHook:
    """
    These are some hooks that run by default, maybe these are created by the
    framework author.
    """
    @hook_impl
    def start(pluggy_example):
        pluggy_example.message = pluggy_example.message.upper()

    @hook_impl
    def stop(pluggy_example):
        print(pluggy_example.message)


class LowerHook:
    """
    This is a new hook that a plugin author has created to modify the behavior
    of the framework to lowercase the message.
    """
    @hook_impl
    def start(pluggy_example):
        pluggy_example.message = pluggy_example.message.lower()


if __name__ == "__main__":
    """
    The user of this framework can apply the hook in their own code without
    changing the behavior of the framework.
    """
    pe = PluggyExample(
        message="hello world",
        hooks=[
            LowerHook,
            DefaultHook,
        ],
    )
    pe.run()
```
