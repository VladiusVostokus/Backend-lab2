import uuid
from flask import Blueprint, request
from marshmallow import ValidationError
from schemas import CategorySchema

categories_bp = Blueprint('categories', __name__)
category_schema = CategorySchema()
category_list_schema = CategorySchema(many=True)
categories = {}

@categories_bp.post("/category")
def add_category():
    try:
        category_data = category_schema.load(request.get_json()) 
    except ValidationError as err:
        return err.messages, 400
    category_id = uuid.uuid4().hex
    category = {"id": category_id, **category_data}
    categories[category_id] = category
    return category_schema.dump(category)

@categories_bp.get("/category/<category_id>")
def get_category(category_id):
    category = categories[category_id]
    if category:
        return category_schema.dump(category)
    return "Category not found", 404

@categories_bp.delete("/category/<category_id>")
def delete_category(category_id):
    category = categories[category_id]
    if category:
        del categories[category_id]
        return category_schema.dump(category)
    return "Category not found", 404