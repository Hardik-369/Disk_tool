from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input
from textual.containers import Container
from textual.screen import Screen
import subprocess

def run_diskpart_script(commands):
    script = '\n'.join(commands)
    with open("temp_script.txt", "w") as f:
        f.write(script)
    result = subprocess.run(["diskpart", "/s", "temp_script.txt"], capture_output=True, text=True)
    return result.stdout.strip()

class MainMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Microsoft Disk Partition Utility", classes="title")
        yield Static("Created by Hardik Kawale", classes="author")
        yield Container(
            Button("> List Disks", id="list", variant="primary"),
            Button("> Clean Disk", id="clean"),
            Button("> Create Partition", id="create"),
            Button("> Exit", id="exit"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "list":
                self.app.push_screen(ListDisksScreen())
            case "clean":
                self.app.push_screen(CleanDiskScreen())
            case "create":
                self.app.push_screen(CreatePartitionScreen())
            case "exit":
                self.app.exit()

class ListDisksScreen(Screen):
    def compose(self) -> ComposeResult:
        output = run_diskpart_script(["list disk"])
        yield Header()
        yield Static("Disk List Output:\n\n" + output, classes="output")
        yield Button("> Back", id="back")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()

class CleanDiskScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Enter Disk Number to Clean:", classes="title")
        yield Input(placeholder="e.g., 1", id="disk_input")
        yield Button("> Clean Disk", id="clean")
        yield Button("> Back", id="back")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "clean":
            disk_num = self.query_one("#disk_input", Input).value
            output = run_diskpart_script([f"select disk {disk_num}", "clean"])
            self.app.push_screen(ResultScreen(f"Disk {disk_num} Cleaned", output))

class CreatePartitionScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Enter Disk Number:", classes="title")
        yield Input(placeholder="e.g., 1", id="disk_input")
        yield Static("Enter Partition Size (MB):", classes="title")
        yield Input(placeholder="e.g., 10240", id="size_input")
        yield Button("> Create Partition", id="create")
        yield Button("> Back", id="back")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "create":
            disk = self.query_one("#disk_input", Input).value
            size = self.query_one("#size_input", Input).value
            output = run_diskpart_script([
                f"select disk {disk}",
                f"create partition primary size={size}",
                "format fs=ntfs quick",
                "assign"
            ])
            self.app.push_screen(ResultScreen("Partition Created", output))

class ResultScreen(Screen):
    def __init__(self, title: str, result: str):
        super().__init__()
        self.title = title
        self.result = result

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(f"{self.title}\n\n{self.result}", classes="output")
        yield Button("> Back to Menu", id="back")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen(to=MainMenu)

class DiskPartitionApp(App):
    CSS = """
    Screen {
        background: black;
        color: white;
        align: center middle;
    }

    Header, Footer {
        background: #222;
        color: white;
        content-align: center middle;
    }

    .title {
        border: round white;
        padding: 1;
        margin: 1;
        text-align: center;
        content-align: center middle;
    }

    .author {
        text-style: italic;
        color: gray;
        text-align: center;
        padding-bottom: 1;
        margin-bottom: 1;
    }

    .output {
        border: round green;
        padding: 1;
        margin: 1;
        color: green;
        background: #111;
        height: auto;
        overflow: auto;
    }

    Button {
        background: #111;
        border: round white;
        color: white;
        padding: 1;
        margin: 1;
    }

    Button.-primary {
        background: #003366;
        color: white;
    }

    Input {
        background: black;
        color: white;
        border: round white;
        padding: 1;
        margin: 1;
    }
    """

    def on_mount(self) -> None:
        self.push_screen(MainMenu())

if __name__ == "__main__":
    DiskPartitionApp().run()
