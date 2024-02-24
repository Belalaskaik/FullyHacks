from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Name(BaseModel):
    name: str

names: List[str] = []

@app.get("/names")
def get_names():
    return {"names": names}

@app.post("/names")
def add_name(name: Name):
    names.append(name.name)
    return {"names": names}
