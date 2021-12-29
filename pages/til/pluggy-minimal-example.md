---
date: 2021-12-31T20:35:27
templateKey: til
title: The most minimal pluggy example
tags:
  - python

---

``` bash
pip install pluggy
```

``` python
import pluggy

HOOK_NAMESPACE = "pluggy_example"
PROJECT_NAME = "pluggy_example"

hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)


class PluggyExampleSpecs:
    @hook_spec
    def start(self, pluggy_example: PluggyExample) -> None:
        pass

    @hook_spec
    def stop(self, pluggy_example: PluggyExample) -> None:
        pass


class PluggyExample:
    def __init__(self, message="", hooks=None) -> None:
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
        self._pm.hook.start(pluggy_example=self)
        self._pm.hook.stop(pluggy_example=self)


class DefaultHook:
    @hook_impl
    def start(pluggy_example):
        pluggy_example.message = pluggy_example.message.upper()

    @hook_impl
    def stop(pluggy_example):
        print(pluggy_example.message)


class LowerHook:
    @hook_impl
    def start(pluggy_example):
        pluggy_example.message = pluggy_example.message.lower()


if __name__ == "__main__":
    pe = PluggyExample(
        message="hello world",
        hooks=[
            LowerHook,
            DefaultHook,
        ],
    )
    pe.run()
```
