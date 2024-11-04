import uuid
from flask import Flask, request
from datetime import datetime
from users import users,users_bp


app = Flask(__name__)

categories = {}
records = {}
app.register_blueprint(users_bp)

@app.post("/category")
def add_category():
    category_data = request.get_json()
    category_id = uuid.uuid4().hex
    category = { "id": category_id, **category_data }
    categories[category_id] = category
    return category

@app.get("/category/<category_id>")
def get_category(category_id):
    category = categories[category_id]
    return category

@app.delete("/category/<category_id>")
def delete_category(category_id):
    category = categories[category_id]
    del categories[category_id]
    return category

@app.post("/record")
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

@app.get("/record/<record_id>")
def get_record(record_id):
    record = records[record_id]
    return record

@app.delete("/record/<record_id>")
def delete_record(record_id):
    record = records[record_id]
    del records[record_id]
    return record

@app.get("/record")
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