import time
from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install
install()


def add_two(n1, n2):
    console.log("About to add two numbers.", log_locals=True)
    return n1 + n2

def print_demo():
    print(f"I wonder what this looks like 1 + 1 = {1 + 1}")
    print({"a": [1,2,3], "b": {"c": 1}})

def style_demo():
    console.print("This is some text.")
    console.print("This is some text.", style="bold")
    console.print("This is some text.", style="bold underline")
    console.print("This is some text.", style="bold underline red")
    console.print("This is some text.", style="bold underline red on white")

def emphasis_demo():
    console.print("[bold]This [underline]is[/] some text.[/]")

def theme_demo():
    console.print("File downloaded!", style="good")
    console.print("File corrupted!", style="bad")
    console.print("The internet is [bad]down![/bad]")

def emoji_demo():
    console.print(":thumbs_up: File downloaded!")

#def log_demo():

#def traceback_demo():

def save_demo():
    try:
        for i in range(3):
            console.log(f"I am about to sleep={i}")
            time.sleep(0.2)
            console.log(f"But I am briefly awake now.")
            add_two(1, i)
        add_two(1, "a")
    except:
        console.print_exception()
    console.save_html("demo.html")

def tables_demo():
    table.add_column("Released", style="cyan")
    table.add_column("Version Number", justify="right", style="magenta")
    table.add_column("Description", style="green")
    table.add_row("May 29, 2020", "v1.0.4", "Just an update.")
    table.add_row("Mar 18, 2020", "v1.0.3", "Just an update.")
    table.add_row("Mar 15, 2020", "v1.0.2", "Just an update.")
    table.add_row("Feb 05, 2020", "v1.0.1", ":thumbs_up: [underline]Big[/] update.")
    console.print(table)

if __name__ == "__main__":
    custome_theme = Theme({
        "good": "green",
        "bad": "bold red"
    })
    console = Console(theme=custome_theme, record=True)
    table = Table(title="Pandas Versions")
    tables_demo()




