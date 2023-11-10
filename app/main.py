import requests
from fastapi import FastAPI
from uploader import file_uploader
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from test_run import test_run
from prueba import predict_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with the origin(s) of your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Hello, World"}

class File(BaseModel):
    url:str

import os

@app.get("/test")
async def test():
    
    notebook_path = './notebooks/pruebas.ipynb'
    test_run(notebook_path)
    return {"message": "Success"}


@app.post("/files/")
async def process_file(url:File):

    r = requests.get(url.url, allow_redirects=True)
    open('../data/SinEtiquetatest_cat_6716.csv', 'wb').write(r.content)
    
    #Sube el resultado del notebook a un archivo
    link = file_uploader()

    return JSONResponse(status_code=200, 
                        content={"message": link})

