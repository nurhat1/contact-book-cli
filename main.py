from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from contact_book import database
from contact_book.model import Contact

app = typer.Typer()
console = Console()


def print_contracts(contacts: List[Contact]) -> None:
    """Print to console given contacts."""
    if len(contacts) == 0:
        console.print("[bold red]No contacts to show[/bold red]")
    else:
        table = Table(
            show_header=True, header_style="bold blue", show_lines=True
        )
        table.add_column("#", style="dim", width=3, justify="center")
        table.add_column("Name", min_width=20, justify="center")
        table.add_column("Contact Number", min_width=12, justify="center")

        for idx, contact in enumerate(contacts, start=1):
            table.add_row(
                str(idx),
                f"[cyan]{contact.name}[/cyan]",
                f"[green]{contact.contact_number}[/green]",
            )

        console.print(table)


@app.command(short_help="Adds a contact")
def add(name: str, contact_number: int):
    """Add a new contact."""
    typer.echo(f"Adding {name}, {contact_number}")

    contact = Contact(name=name, contact_number=contact_number)
    database.create(contact)
    show()


@app.command(short_help="Shows all contacts")
def show():
    """Show all contacts."""
    contacts = database.read()

    console.print("[bold magenta]Contact Book[/bold magenta]", "📕")

    print_contracts(contacts)


@app.command(short_help="Edits a contact")
def edit(
    position: int,
    name: Optional[str] = None,
    contact_number: Optional[int] = None,
):
    """Edit a contact with the given position."""
    typer.echo(f"Editing {position}")

    database.update(
        position=position, name=name, contact_number=contact_number
    )
    show()


@app.command(short_help="Removes a contact")
def remove(position: int):
    """Delete a contact with the given position."""
    typer.echo(f"Removing {position}")

    database.delete(position=position)
    show()


@app.command(short_help="Searches a contact")
def search(name: str):
    """Search contacts with the given name."""
    typer.echo(f"Searching {name}")

    contacts = database.search(name=name)

    print_contracts(contacts)


if __name__ == "__main__":
    app()
