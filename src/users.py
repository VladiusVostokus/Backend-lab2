import uuid
from flask import Blueprint, request

users_bp = Blueprint('users', __name__)
users = {}

@users_bp.post("/user")
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, **user_data}
    users[user_id] = user
    return user

@users_bp.get("/users")
def get_users():
    return list(users.values())

@users_bp.get("/user/<user_id>")
def get_user(user_id):
    user = users[user_id]
    if user:
        return user
    return "User not found", 404

@users_bp.delete("/user/<user_id>")
def delete_user(user_id):
    user = users[user_id]
    if user:
        del users[user_id]
        return user
    return "User not found", 404
    