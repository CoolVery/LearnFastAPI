from fastapi import FastAPI

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