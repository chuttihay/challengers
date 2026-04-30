from typing import List, Optional

from backend.db_stub.fake_db import FAKE_USERS
from backend.models.user import User


class UserQueryRepository:

    @staticmethod
    def get_by_id(user_id: str) -> Optional[User]:
        for user in FAKE_USERS:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def get_by_email(email: str) -> Optional[User]:
        for user in FAKE_USERS:
            if user.email == email:
                return user
        return None

    @staticmethod
    def list_users(limit: int = 50, offset: int = 0) -> List[User]:
        return FAKE_USERS[offset:offset + limit]