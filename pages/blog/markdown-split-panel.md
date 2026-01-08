---
date: 2025-02-03 13:21:23
templateKey: blog-post
title: markdown split panel
tags:
  - blog
  - markdown
published: True

---

Today I was playing with markdown split panels.  I want to be able to compare
and constrast occasionually, today the inspiration hit to do this using
admonitions.

<!-- ![screenshot-2025-02-04T02-28-26-951Z.png](https://dropper.waylonwalker.com/api/file/46ead069-5731-4028-886a-f76d56792691.png){.more-cinematic} -->

![screenshot-2025-02-04T02-28-46-750Z.png](https://dropper.waylonwalker.com/api/file/e3d40c22-643d-433c-8eb4-c3ddf91d0527.png){.more-cinematic}

{.rounded-xl }
!!! Note Mobile Users 🔄

    You will need to rotate your device to see the side by side feature.

## The Markdown

This is what I am going for, one admonition that is easy to remember, that
nests inside of itself , and I can put as much markdown on the inside that I
want.

``` markdown
!!! vsplit I Have two opinions

    !!! vsplit Left Opinion

        supporting arguments

        * lorem ipsum
        * ipsum dolor

        - [x] lorem ipsum
        - [ ] ipsum dolor

    !!! vsplit Right Opinion

        supporting arguments

        * lorem ipsum
        * ipsum dolor

        - [ ] lorem ipsum
        - [x] ipsum dolor
```

Here is the result of that markdown.

!!! vsplit I Have two opinions

    !!! vsplit Left Opinion

        supporting arguments

        * lorem ipsum
        * ipsum dolor

        - [x] lorem ipsum
        - [ ] ipsum dolor

    !!! vsplit Right Opinion

        supporting arguments

        * lorem ipsum
        * ipsum dolor

        - [ ] lorem ipsum
        - [x] ipsum dolor

{.clean}
!!! vsplit ""

    !!! vsplit Hello World

        Here is a hello world application written in the typer cli framework
        for cli.

    !!! vsplit ""
        ``` python
        #!/usr/bin/env -S uv run --quiet --script
        # ///
        # requires-python = ">=3.12"
        # dependencies = [
        #     "typer",
        # ]
        # ///

        import typer

        app = typer.Typer()

        @app.command()
        def hello(name: str = "World"):
            """Prints a greeting message."""
            typer.echo(f"Hello, {name}!")

        if __name__ == "__main__":
            app()
        ```
