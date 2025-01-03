import uuid
from flask import Blueprint, request
from marshmallow import ValidationError
from schemas import PlainUserSchema
from models import db, UserModel

users_bp = Blueprint('users', __name__)
user_schema = PlainUserSchema()
user_list_schema = PlainUserSchema(many=True)

@users_bp.post("/user")
def create_user():
    try:
        user_data = user_schema.load(request.get_json())
    except ValidationError as err:
        return err.messages, 400
    user = UserModel(id=uuid.uuid4(), **user_data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)

@users_bp.get("/users")
def get_users():
    all_users = UserModel.query.all()
    return user_list_schema.dump(all_users)

@users_bp.get("/user/<user_id>")
def get_user(user_id):
    user = UserModel.query.get(user_id)
    if user:
        return user_schema.dump(user)
    return "User not found", 404

@users_bp.delete("/user/<user_id>")
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user)
    return "User not found", 404