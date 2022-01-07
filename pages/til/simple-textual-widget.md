---
date: 2022-01-07 03:25:36.794864
templateKey: til
title: Making a Textual Widget from a Rich Renderable
tags:
  - python
  - cli

---

Once you have made your sick looking cli apps with rich, eventually you are
going to want to add some keybindings to them.  Currently Textual, also written
by [@willmcgugan](https://twitter.com/willmcgugan), does this extremely well.
Fair Warning it is in super beta mode and expected to change a bunch.  So take
it easy with hopping on the train so fast.

## Get the things


Install them from the command line.

``` bash
pip install textual
pip install rich
```

Import make a .py file and import them in it.

``` python
from textual.app import App
from textual.widget import Widget
from rich.panel import Panel
```

## Make what you have a widget

If you return your rich renderable out of class that inherits from
`textual.widget.Widget`, you can then dock this inside of an app class
inheriting from `textual.app.App`.

``` python
class MyWidget(Widget):
    def render(self):
        my_renderable = Panel("press q to quit")
        return my_renderable

class MyApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(MyWidget(), edge="top")
        await self.bind("q", "quit")
```

## run it

You've made a TUI (text user interface).  Run the classmethod `run` to display
the it in its full screen glory.

``` python
MyApp.run(log="textual.log")
```

## Final result

At this point It probably does not look much different, but it can be
interactive by binding keys to any method on your app that starts with the word
`action_`, this includes the built-in actions such as `action_quit`.

``` python
from textual.app import App
from textual.widget import Widget
from rich.panel import Panel


class MyWidget(Widget):
    def render(self):
        my_renderable = Panel("press q to quit")
        return my_renderable


class MyApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(MyWidget(), edge="top")
        await self.bind("q", "quit")


if __name__ == "__main__":
    MyApp.run(log="textual.log")
```
