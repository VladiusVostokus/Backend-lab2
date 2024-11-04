import uuid
from flask import Blueprint, request

categories_bp = Blueprint('categories', __name__)
categories = {}

@categories_bp.post("/category")
def add_category():
    category_data = request.get_json()
    category_id = uuid.uuid4().hex
    category = {"id": category_id, **category_data}
    categories[category_id] = category
    return category

@categories_bp.get("/category/<category_id>")
def get_category(category_id):
    category = categories[category_id]
    return category

@categories_bp.delete("/category/<category_id>")
def delete_category(category_id):
    category = categories[category_id]
    del categories[category_id]
    return category