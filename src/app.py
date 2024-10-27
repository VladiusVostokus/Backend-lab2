import uuid
from flask import Flask, request

app = Flask(__name__)

users = {}

@app.post("/user")
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = { "id": user_id, **user_data }
    users[user_id] = user
    return user

@app.get("/users")
def get_users():
    return list(users.values())
