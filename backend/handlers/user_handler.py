from typing import Dict

from backend.repositories.queries.postgres_query_repository import dummy_query_response


async def get_user_information_handler(user_id: str):
    ret: Dict = await dummy_query_response(user_id)
    return ret