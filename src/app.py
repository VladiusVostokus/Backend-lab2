import uuid
from flask import Flask, request

app = Flask(__name__)

users = {}
categories = {}

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

@app.get("/user/<user_id>")
def get_user(user_id):
    user = users[user_id]
    return user

@app.delete("/user/<user_id>")
def delete_user(user_id):
    user = users[user_id]
    del users[user_id]
    return user

@app.post("/category")
def add_category():
    category_data = request.get_json()
    category_id = uuid.uuid4().hex
    category = { "id": category_id, **category_data }
    categories[category_id] = category
    return category