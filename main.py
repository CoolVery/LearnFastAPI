from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Start to learn:)"
)

data_users = [
    {"id": 1, "role": "admin", "name": "Alice"},
    {"id": 2, "role": "editor", "name": "Bob"},
    {"id": 3, "role": "subscriber", "name": "Charlie"},
    {"id": 4, "role": "moderator", "name": "Diana"},
    {"id": 5, "role": "viewer", "name": "Ethan"}
]

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return [user for user in data_users if user.get('id') == user_id]

@app.get("/user_cut")
def get_cut_user(limit: int = 3, offset: int = 0):
    return data_users[offset:limit]

@app.post("/user/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, data_users))[0]
    current_user["name"] = new_name
    return {"status": 200, "source": current_user}

data_trades = [
    {"id": 1, "user_id": 1, "currency": "USD", "side": "buy", "price": 100.50, "amount": 1.5},
    {"id": 2, "user_id": 1, "currency": "EUR", "side": "sell", "price": 200.75, "amount": 2.0},
    {"id": 3, "user_id": 2, "currency": "GBP", "side": "buy", "price": 300.00, "amount": 3.5},
    {"id": 4, "user_id": 3, "currency": "JPY", "side": "sell", "price": 400.25, "amount": 4.1},
    {"id": 5, "user_id": 4, "currency": "AUD", "side": "buy", "price": 500.60, "amount": 2.8}
]
class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float
@app.post("/trades")
def add_trades(trades: List[Trade]):
    data_trades.extend(trades)
    return {"status": 200, "source": data_trades}