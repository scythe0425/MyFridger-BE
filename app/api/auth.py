from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/callback")
async def auth_callback(code: str, state: str, uri: str):
    return {"message": "Auth callback test"}

@router.post("/auth/login")
async def login(username: str, password: str):
    return {"message": "Login test"}
