from typing import List, Optional

from contact_book import ContactQuery, db
from contact_book.model import Contact


def create(contact: Contact) -> None:
    """Create a new contact."""
    contact.position = len(db) + 1
    new_contact = {
        "name": contact.name,
        "contact_number": contact.contact_number,
        "position": contact.position,
        "created_at": contact.created_at,
        "updated_at": contact.updated_at,
    }

    db.insert(new_contact)


def read() -> List[Contact]:
    """Get all contacts."""
    results = db.all()

    contacts = [
        Contact(
            name=result["name"],
            contact_number=result["contact_number"],
            position=result["position"],
            created_at=result["created_at"],
            updated_at=result["updated_at"],
        )
        for result in results
    ]

    return contacts


def update(
    position: int,
    name: Optional[str] = None,
    contact_number: Optional[int] = None,
) -> None:
    """Update a contact with given position."""
    if all([name, contact_number]):
        db.update(
            {"name": name, "contact_number": contact_number},
            ContactQuery.position == position,
        )
    elif name is not None:
        db.update({"name": name}, ContactQuery.position == position)
    elif contact_number is not None:
        db.update(
            {"contact_number": contact_number},
            ContactQuery.position == position,
        )


def delete(position: int) -> None:
    """Delete contact with given position."""
    count = len(db)

    db.remove(ContactQuery.position == position)

    for pos in range(position + 1, count):
        change_position(pos, pos - 1)


def change_position(old_position: int, new_position: int) -> None:
    """Change old position with the new one."""
    db.update(
        {"position": new_position}, ContactQuery.position == old_position
    )


def search(name: str) -> List[Contact]:
    """Search contacts with the given name."""
    results = db.search(ContactQuery.name == name)

    contacts = [
        Contact(
            name=result["name"],
            contact_number=result["contact_number"],
            position=result["position"],
            created_at=result["created_at"],
            updated_at=result["updated_at"],
        )
        for result in results
    ]

    return contacts
