import uuid
from datetime import datetime
from flask import Blueprint, request
from marshmallow import ValidationError
from schemas import RecordSchema
from models import db, UserModel, CategoryModel, RecordModel, AccountModel

records_bp = Blueprint('records', __name__)
record_schema = RecordSchema()
record_list_schema = RecordSchema(many=True)

@records_bp.post("/record")
def create_record():
    try:
        record_data = record_schema.load(request.get_json())
    except ValidationError as err:
        return err.messages, 400

    user = UserModel.query.get(record_data["user_id"])
    if not user:
        return "Incorrect user_id: user does not exist", 400

    category = CategoryModel.query.get(record_data["category_id"])
    if not category:
        return "Incorrect category_id: category does not exist", 400
    
    account = AccountModel.query.get(user.account_id)
    if not account:
        return "User has no account", 400
    
    record = RecordModel(
        id=uuid.uuid4().hex,
        user_id=record_data["user_id"],
        category_id=record_data["category_id"],
        date=datetime.now(),
        **{key: value for key, value in record_data.items() if key not in ["user_id", "category_id"]}
    )
    expence = record_data["expense"]
    new_balance = float(account.balance) - float(expence)
    
    account.balance = str(new_balance)
    db.session.add(record)
    db.session.commit()

    return record_schema.dump(record), 201

@records_bp.get("/record/<record_id>")
def get_record(record_id):
    record = RecordModel.query.get(record_id)
    if record:
        return record_schema.dump(record), 200
    return "Record not found", 404

@records_bp.delete("/record/<record_id>")
def delete_record(record_id):
    record = RecordModel.query.get(record_id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return record_schema.dump(record), 200
    return "Record not found", 404

@records_bp.get("/record")
def get_record_by_category_and_user():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')

    if (user_id != None and category_id != None):
        result = find_by_user_and_category(user_id,category_id)
        if not result:
            return "Record not found", 404
        return record_schema.dump(result)
     
    if (user_id != None):
        result = find_by_user(user_id)
        if result == []:
            return "Record not found", 404
        return record_list_schema.dump(result)
    
    if (category_id != None):
        result = find_by_category(category_id)
        if result == []:
            return "Record not found", 404
        return record_list_schema.dump(result)
    
    return "No parameters provided", 400


def find_by_user_and_category(user_id, category_id):
    return RecordModel.query.filter_by(user_id=user_id, category_id=category_id).first()

def find_by_user(user_id):
    return RecordModel.query.filter_by(user_id=user_id).all()

def find_by_category(category_id):
    return RecordModel.query.filter_by(category_id=category_id).all()