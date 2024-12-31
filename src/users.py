import uuid
from flask import Blueprint, request
from marshmallow import ValidationError
from schemas import PlainUserSchema

users_bp = Blueprint('users', __name__)
user_schema = PlainUserSchema()
user_list_schema = PlainUserSchema(many=True)
users = {}

@users_bp.post("/user")
def create_user():
    try:
        user_data = user_schema.load(request.get_json()) 
    except ValidationError as err:
        return err.messages, 400
    user_id = uuid.uuid4().hex
    user = {"id": user_id, **user_data}
    users[user_id] = user
    return user_schema.dump(user)

@users_bp.get("/users")
def get_users():
    all_users = list(users.values())
    return user_list_schema.dump(all_users)

@users_bp.get("/user/<user_id>")
def get_user(user_id):
    user = users[user_id]
    if user:
        return user_schema.dump(user)
    return "User not found", 404

@users_bp.delete("/user/<user_id>")
def delete_user(user_id):
    user = users[user_id]
    if user:
        del users[user_id]
        return user_schema.dump(user)
    return "User not found", 404