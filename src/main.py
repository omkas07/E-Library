from fastapi import FastAPI
from src.presentation.api import auth_api
from src.presentation.api import auth_admin_api

app = FastAPI()

app.include_router(auth_api.router, prefix="/api")
app.include_router(auth_admin_api.router, prefix="/api")