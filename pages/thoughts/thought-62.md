---
title: '💭 Center things - Textual'
date: 2023-07-30T16:31:55
template: link
link: https://textual.textualize.io/how-to/center-things/
tags:
  - python
  - textual
  - tui
  - thoughts
  - thought
  - link
published: true

---

![[https://textual.textualize.io/how-to/center-things/]]

How to center things in textual. Textual has a very unique way of styling text user interfaces for the terminal using css.  If you know css it feels natural.

@willmcgugan, has put together a great article on how to center things in textual

here the final result


``` python
from textual.app import App, ComposeResult
from textual.widgets import Static

QUOTE = "Could not find you in Seattle and no terminal is in operation at your classified address."


class CenterApp(App):
    """How to center things."""

    CSS = """
    Screen {
        align: center middle;
    }

    #hello {
        background: blue 50%;
        border: wide white;
        width: 40;
        height: 9;
        text-align: center;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(QUOTE, id="hello")


if __name__ == "__main__":
    app = CenterApp()
    app.run()
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
