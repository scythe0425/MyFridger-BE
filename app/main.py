from fastapi import FastAPI
from app.api import auth, user  # app 디렉토리 내 라우터 모듈 import

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
