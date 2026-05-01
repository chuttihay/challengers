from fastapi import APIRouter, HTTPException

from backend.handlers.user_handler import UserHandler

router = APIRouter()


@router.post("/users")
async def create_user(email: str, name: str):
    try:
        return await UserHandler.create_user(email, name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await UserHandler.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users")
async def list_users():
    return UserHandler.list_users()


@router.put("/users/{user_id}")
async def update_user(user_id: str, name: str):
    user = await UserHandler.update_user(user_id, name=name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    success = await UserHandler.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}