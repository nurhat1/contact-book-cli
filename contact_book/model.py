from datetime import datetime
from typing import Optional


class Contact:
    def __init__(
        self,
        name: str,
        contact_number: int,
        position: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.name = name
        self.contact_number = contact_number
        self.position = position
        self.created_at = (
            created_at
            if created_at is not None
            else datetime.now().isoformat()
        )
        self.updated_at = (
            updated_at
            if updated_at is not None
            else datetime.now().isoformat()
        )

    def __repr__(self) -> str:
        return "Contact(name={}, contact_number={}, position={}, created_at={}, updated_at={})".format(
            self.name,
            self.contact_number,
            self.position,
            self.created_at,
            self.updated_at,
        )
