from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.jwt_manager import create_token
from schema.user import User2

user_router = APIRouter()


# endpoint de usuarios


@user_router.post('/login', tags=["auth"])
def login(user: User2):
    if user.username == 'admin' and user.password == 'admin':
        token = create_token(user.dict())
        return JSONResponse(content={'token': token}, status_code=200)
