from fastapi import FastAPI, Query, Depends
from typing import Dict

app = FastAPI()

@app.get('/', tags=['Root'])
def home_page() -> Dict[str, str]:
    return {'home_page': 'Welcome to this Blog Application'}

@app.get('/bye', tags=['BYE'])
def bye_page() -> Dict[str, str]:
    return {'bye_page': 'BYE!!!'}