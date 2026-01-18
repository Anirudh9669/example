# scorer.py

def calculate_score(surface: float, rooms: int) -> float:
    """
    The core scoring algorithm. 
    Separated from the API logic.
    """
    # The logic used is base price + (surface * multiplier) + (rooms * bonus), like a weighted sum.
    base_price = 100000
    price = base_price + (surface * 4000) + (rooms * 16250)
    return price