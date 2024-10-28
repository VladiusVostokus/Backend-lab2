import uuid
from flask import Flask, request
from datetime import datetime


app = Flask(__name__)

users = {}
categories = {}
records = {}

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
    record_id = uuid.uuid4().hex
    now = datetime.now()
    date = now.isoformat('T')
    record = { "id": record_id, **record_data, "date": date }
    records[record_id] = record
    return record