from fastapi import FastAPI
from pydantic import BaseModel
class Guna(BaseModel):
    age=19
    reg=6117
    
nsit=FastAPI()

@nsit.get("/{Name:path}")
def guna(Name:str):
     return{"Narasu's Sarathy Institute Of Technology":Name}

@nsit.post("/item")
def reg(i:Guna):return(i)
