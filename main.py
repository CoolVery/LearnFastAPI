from fastapi import FastAPI
from fastapi_users import fastapi_users
from pydantic import BaseModel, Field

from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Start to learn:)"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)