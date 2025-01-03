import uuid
from flask import Blueprint, request
from marshmallow import ValidationError
from schemas import PlainUserSchema, AccountSchema
from models import db, UserModel, AccountModel

users_bp = Blueprint('users', __name__)
user_schema = PlainUserSchema()
user_list_schema = PlainUserSchema(many=True)
account_schema = AccountSchema()

@users_bp.post("/user")
def create_user():
    try:
        user_data = user_schema.load(request.get_json())
    except ValidationError as err:
        return err.messages, 400

    user_id = uuid.uuid4()
    account_id = uuid.uuid4()
    account = AccountModel(id=account_id, user_id=user_id, balance="0")
    user = UserModel(id=user_id, name=user_data['name'], account_id=account_id) 
    db.session.add(account)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)

@users_bp.put("/account/<account_id>")
def top_up_account(account_id):
    account = AccountModel.query.get(account_id)
    if not account:
        return "Account not fount", 404
    data = request.get_json()
    balance = data['balance']
    if not balance:
        return "Balance required", 400
    
    account.balance = float(account.balance) + float(balance)
    db.session.commit()
    return account_schema.dump(account)

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
        account = AccountModel.query.filter_by(user_id=user_id).first()
        db.session.delete(account)
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user)
    return "User not found", 404