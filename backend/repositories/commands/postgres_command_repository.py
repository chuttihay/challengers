from typing import Optional
from datetime import datetime

from backend.models.user import User
from backend.db_stub.fake_db import FAKE_USERS


class UserCommandRepository:

    @staticmethod
    def create(email: str, name: str) -> User:
        user = User.fake(email=email, name=name)
        FAKE_USERS.append(user)
        return user

    @staticmethod
    def update(user_id: str, **kwargs) -> Optional[User]:
        for user in FAKE_USERS:
            if user.id == user_id:
                for key, value in kwargs.items():
                    if hasattr(user, key):
                        setattr(user, key, value)

                user.updated_at = datetime.utcnow()
                return user
        return None

    @staticmethod
    def delete(user_id: str) -> bool:
        before = len(FAKE_USERS)
        FAKE_USERS[:] = [u for u in FAKE_USERS if u.id != user_id]
        return len(FAKE_USERS) < before