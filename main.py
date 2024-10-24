from rich.text import Text
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Header


class GhDash(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

    def on_mount(self) -> None:
        self.title = "ghdash"
        self.sub_title = "What's on your plate today? 🍽️"

def entrypoint():
    app = GhDash()
    app.run()

if __name__ == "__main__":
    entrypoint()
