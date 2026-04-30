from typing import Dict

from fastapi import HTTPException, APIRouter

from backend.handlers.user_handler import get_user_information_handler

router = APIRouter()

@router.get("/user/get_user_info")
async def get_user_info(user_id: str):
    try:
        response: Dict = await get_user_information_handler(user_id=user_id)
        return response
    except Exception as e:
        raise HTTPException(500, f"Backend Error: {e}")