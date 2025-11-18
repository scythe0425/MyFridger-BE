from fastapi import APIRouter

router = APIRouter()

@router.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.post("/user")
async def create_user(username: str, password: str):
    return {"message": f"User {username} created"}
