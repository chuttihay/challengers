from typing import Optional, List

from backend.models.user import User
from backend.repositories.commands.postgres_command_repository import UserCommandRepository
from backend.repositories.queries.postgres_query_repository import UserQueryRepository


class UserHandler:

    # --- READS ---

    @staticmethod
    async def get_user(user_id: str) -> Optional[User]:
        return UserQueryRepository.get_by_id(user_id)

    @staticmethod
    async def list_users(limit: int = 50, offset: int = 0) -> List[User]:
        return UserQueryRepository.list_users(limit=limit, offset=offset)

    # --- WRITES ---

    @staticmethod
    async def create_user(email: str, name: str) -> User:
        # basic validation
        if not email or "@" not in email:
            raise ValueError("Invalid email")

        # business rule: email must be unique
        existing = UserQueryRepository.get_by_email(email)
        if existing:
            raise ValueError("User with this email already exists")

        return UserCommandRepository.create(email=email, name=name)

    @staticmethod
    async def update_user(user_id: str, **kwargs) -> Optional[User]:
        user = UserQueryRepository.get_by_id(user_id)
        if not user:
            return None

        # optional: enforce allowed fields
        allowed_fields = {"name"}
        updates = {k: v for k, v in kwargs.items() if k in allowed_fields}

        if not updates:
            return user

        return UserCommandRepository.update(user_id, **updates)

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        user = UserQueryRepository.get_by_id(user_id)
        if not user:
            return False

        return UserCommandRepository.delete(user_id)