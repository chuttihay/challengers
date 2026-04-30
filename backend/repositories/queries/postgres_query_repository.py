import random
from typing import Dict


async def dummy_query_response(user_id: str) -> Dict:
    resp = {
        "user_id": user_id,
        "age": random.randint(22, 30),
        "gender": "female",
        "name": "Nick"
    }
    return resp
