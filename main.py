from textual.app import App, ComposeResult
from textual.widgets import Header, Placeholder


class GhDash(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Placeholder("Hello", classes="thing")
        yield Placeholder("Hello", classes="thing")

    def on_mount(self) -> None:
        self.title = "ghdash"
        self.sub_title = "What's on your plate today? 🍽️"


def entrypoint():
    app = GhDash()
    app.run()


if __name__ == "__main__":
    entrypoint()
