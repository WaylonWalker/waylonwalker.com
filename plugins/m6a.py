from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Footer, Input, Static
from rich.panel import Panel
from markata import Markata
from rich.table import Table


class MarkataTUI(App):
    CSS_PATH = "style.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
        (":", "focus_command", "Command Mode"),
        ("escape", "blur", "Exit Command Mode"),
    ]

    def __init__(self):
        super().__init__()
        self.m = Markata()
        self.m.run()
        self.command_input = Input(placeholder=":command")
        self.output = Static("Welcome to Markata TUI", id="output")

    def compose(self) -> ComposeResult:
        # yield Header(show_clock=True)
        yield Static(
            f"[bold]Site:[/] {self.m.config.site_name} \n[bold]Author:[/] {self.m.config.author_name} <{self.m.config.author_email}>",
            id="meta",
        )
        with VerticalScroll(id="main"):
            yield self.command_input
            yield self.output
        yield Footer()

    def action_focus_command(self):
        self.set_focus(self.command_input)

    def action_blur(self):
        self.set_focus(None)

    def on_input_submitted(self, message: Input.Submitted) -> None:
        command = message.value.strip()

        if command == "plugins" or command == "plug":
            plugins = [p.__name__ for p in self.m._pm.get_plugins()]
            self.output.update(Panel("\n".join(plugins), title="Plugins"))

        elif command == "posts":
            if not self.m.posts:
                self.output.update("No posts found.")
                return
            table = Table()
            include = [
                "title",
                "published",
                "slug",
                "date",
                "tags",
                "templateKey",
            ]
            for field in include:
                table.add_column(field)
            for post in self.m.posts:
                table.add_row(*(str(getattr(post, f)) for f in include))

            self.output.update(table)

        elif command == "feeds" or command == "feed":
            feeds = [f"{k}: {len(v.posts)} posts" for k, v in self.m.feeds.items()]
            self.output.update(Panel("\n".join(feeds), title="Feeds"))

        elif command == "templates" or command == "template":
            loaders = getattr(self.m.template_env, "loader", None)
            if hasattr(loaders, "loaders"):
                paths = [
                    getattr(l, "searchpath", ["unknown"])[0] for l in loaders.loaders
                ]
            else:
                paths = getattr(loaders, "searchpath", ["unknown"])
            self.output.update(Panel("\n".join(paths), title="Template Paths"))

        else:
            self.output.update(f"Unknown command: {command}")

        self.command_input.value = ""
        self.set_focus(None)


if __name__ == "__main__":
    app = MarkataTUI()
    app.run()
