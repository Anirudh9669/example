# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from scorer import calculate_score

app = FastAPI()

class FlatData(BaseModel):
    address: str
    surface: float
    rooms: int

@app.get("/")
def home():
    return {"message": "This is a Flat Price Scorer"}

@app.post("/score")
def get_score(data: FlatData):
    # Calling the function by passing parameters of surface and rooms.
    estimated_price = calculate_score(data.surface, data.rooms)
    
    return {
        "address": data.address,
        "estimated_price": estimated_price,
        "features_used": {
            "surface": data.surface,
            "rooms": data.rooms
        }
    }