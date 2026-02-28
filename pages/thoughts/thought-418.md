---
title: '💭 Document how to provide a negative number as an argument · fas...'
date: 2024-10-30T01:28:56
template: link
link: https://github.com/fastapi/typer/discussions/798
tags:
  - python
  - cli
  - typer
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/fastapi/typer/discussions/798]]

Today I learned that you cannot pass negative integers as values to typer.  in this case `context_settings={"ignore_unknown_options": True}` is required so that the `-` does not look like a flag.

``` python
# script name: main.py

import typer

app = typer.Typer()


@app.command()
def failing(value: float):
    print(f"{value=}")
    

@app.command(
    context_settings={"ignore_unknown_options": True}
)
def working_good(value: float):
    print(f"{value=}")
    
    
if __name__ == "__main__":
    app()
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
