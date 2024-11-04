import uuid
from datetime import datetime
from flask import Blueprint, request
from users import users
from categories import categories

records_bp = Blueprint('records', __name__)
records = {}


@records_bp.post("/record")
def create_record():
    record_data = request.get_json()
    if (record_data["user_id"] not in users):
        return "Incorrect user id: user does not exist", 400
    if (record_data["category_id"] not in categories):
        return "Incorrect category id: category does not exist", 400
    record_id = uuid.uuid4().hex 
    now = datetime.now()
    date = now.isoformat('T')
    record = { "id": record_id, **record_data, "date": date }
    records[record_id] = record
    return record

@records_bp.get("/record/<record_id>")
def get_record(record_id):
    record = records[record_id]
    return record

@records_bp.delete("/record/<record_id>")
def delete_record(record_id):
    record = records[record_id]
    del records[record_id]
    return record

@records_bp.get("/record")
def get_record_by_category_and_user():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')

    if (user_id != None and category_id != None):
        result = find_by_user_and_category(user_id,category_id)
        return result  
    if (user_id != None):
        result = find_by_user(user_id)
        return result  
    if (category_id != None):
        result = find_by_category(category_id)
        return result
    return "No parameters provided", 400


def find_by_user_and_category(user_id, category_id):
    result = {}
    for id in records:
        record = records[id]
        if record["user_id"] == user_id or record["category_id"] == category_id:
            result = record
    return result

def find_by_user(user_id):
    result = []
    for id in records:
        record = records[id]
        if record["user_id"] == user_id:
            result.append(record)
    return result

def find_by_category(category_id):
    result = []
    for id in records:
        record = records[id]
        if record["category_id"] == category_id:
            result.append(record)
    return result