from fastapi import FastAPI, Query, Depends
from typing import Dict
from server.routes.student import router as StudentRouter

app = FastAPI()


# @app.get('/bye', tags=['BYE'])
# def bye_page() -> Dict[str, str]:
#     return {'bye_page': 'BYE!!!'}
@app.get('/', tags=['Root'])
def home_page() -> Dict[str, str]:
    return {'home_page': 'Welcome to this Blog Application'}

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
