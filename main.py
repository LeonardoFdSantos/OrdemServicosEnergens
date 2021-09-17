from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import databases
import sqlalchemy
from datetime import datetime


app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello World!"}