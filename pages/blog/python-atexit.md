---
date: 2000-01-15 23:45:55.942093
templateKey: til
title: Python atexit
tags:
  - python
published: false
---

I'm still trying to understand this one, but this is how you force a
python object to stop atexit.

```python
import atexit

class Server:
    def __init__(
        self,
        auto_restart: bool = True,
        directory: Union[str, "Path"] = None,
        port: int = 8000,
    ):
        if directory is None:
            from markata import Markata

            m = Markata()
            directory = m.config["output_dir"]

        self.directory = directory
        self.port = find_port(port=port)
        self.start_server()
        atexit.register(self.kill)

    def start_server(self):
        import subprocess

        self.cmd = [
            "python",
            "-m",
            "http.server",
            str(self.port),
            "--directory",
            self.directory,
        ]

        self.proc = subprocess.Popen(
            self.cmd,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        self.start_time = time.time()


    def kill(self):
        self.auto_restart = False
        self.proc.kill()

    def __rich__(self) -> Panel:
        if not self.proc.poll():
            return Panel(
                f"[green]serving on port: [gold1]{self.port} [green]using pid: [gold1]{self.proc.pid} [green]uptime: [gold1]{self.uptime} [green]link: [gold1] http://localhost:{self.port}[/]",
                border_style="blue",
                title="server",
            )

        else:
            if self.auto_restart:
                self.start_server()

            return Panel(f"[red]server died", title="server", border_style="red")
```
