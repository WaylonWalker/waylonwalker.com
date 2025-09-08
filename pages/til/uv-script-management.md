---
date: 2025-09-07 20:22:56
templateKey: til
title: uv script management
published: true
tags:
  - python

---


I've been leaning on
[lazy-self-installing-python-scripts](https://treyhunner.com/2024/12/lazy-self-installing-python-scripts-with-uv/)
more and more, but I did not realize how much tooling that
[uv](https://docs.astral.sh/uv/getting-started/installation/)
gives you to help manage your scripts.

``` bash
uv init --script up
uv add --script up typer rich
uv remove --script up rich
sed -i '1i #!/usr/bin/env -S uv run --script' up
chmod +x up
./up
```

The result is a script that looks like this, its executable as what looks like
regular command in your shell.

``` python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "typer",
# ]
# ///


def main() -> None:
    print("Hello from up!")


if __name__ == "__main__":
    main()
```
