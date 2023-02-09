from fastapi import FastAPI
from typing import Dict
from server.routes.user import router as UserRouter

app = FastAPI()


@app.get('/', tags=['Root'])
def home_page() -> Dict[str, str]:
    return {'home_page': 'Welcome to this CRUD Application'}

@app.get('/bye', tags=['Bye'])
def bye_page() -> Dict[str, str]:
    return {'bye_page': 'BYE!!!'}

app.include_router(UserRouter, tags=["Users"], prefix="/user")
