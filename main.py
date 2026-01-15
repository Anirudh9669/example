from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# This defines what your API expects to receive
class FlatRequest(BaseModel):
    address: str
    surface: float
    rooms: Optional[int] = None

@app.get("/")
def home():
    return {"message": "Flat Price Scorer is Online"}

@app.post("/score")
def score_flat(flat: FlatRequest):
    # ML Logic Placeholder
    # In MLOps, you'd load a model here: model.predict([[surface, rooms]])
    price_per_meter = 5000
    estimated_price = flat.surface * price_per_meter
    
    if flat.rooms:
        estimated_price += (flat.rooms * 10000)
        
    return {
        "address": flat.address,
        "estimated_price": estimated_price,
        "features_used": {
            "surface": flat.surface,
            "rooms": flat.rooms
        }
    }