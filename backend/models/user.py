from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class User:
    id: str
    email: str
    name: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def fake(email: str, name: str):
        now = datetime.utcnow()
        return User(
            id=str(uuid.uuid4()),
            email=email,
            name=name,
            created_at=now,
            updated_at=now
        )