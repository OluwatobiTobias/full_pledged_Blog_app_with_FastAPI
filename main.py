from fastapi import FastAPI
from typing import Dict
import uvicorn

app = FastAPI()

@app.get('/')
def home_page() -> Dict[str, str]:
    return {'home_page': 'OK..., all is good.'}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)