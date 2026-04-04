from fastapi import FastAPI
from src.presentation.api import user_api

app = FastAPI()

app.include_router(user_api.router, prefix="/api/users")