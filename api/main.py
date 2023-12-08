from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}

def start():
    uvicorn.run("api.main:app", host = "127.0.0.1")