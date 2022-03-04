from fastapi import FastAPI
from pydantic import BaseModel
class Dinesh(BaseModel):
    age=19
    Date of birth=06-05-2003
    College code=6117
    Register number=611720104022

nsit=FastAPI()

@nsit.get("/{Name:path}")
def guna(Name:str):
     return{"Narasu's Sarathy Institute Of Technology":Name}

@nsit.post("/item")
def reg(i: Dinesh):return(i)
