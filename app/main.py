from app import *
from fastapi import FastAPI


createDB()

app = FastAPI()

@app.get("/")
def hi():
    return{"smthin"}


