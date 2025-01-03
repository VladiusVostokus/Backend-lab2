import uuid
from flask import Blueprint, request
from marshmallow import ValidationError
from schemas import CategorySchema
from models import db, CategoryModel
from models import RecordModel

categories_bp = Blueprint('categories', __name__)
category_schema = CategorySchema()
category_list_schema = CategorySchema(many=True)

@categories_bp.post("/category")
def add_category():
    try:
        category_data = category_schema.load(request.get_json()) 
    except ValidationError as err:
        return err.messages, 400
    category = CategoryModel(id=uuid.uuid4(), **category_data)
    db.session.add(category)
    db.session.commit()
    return category_schema.dump(category)

@categories_bp.get("/category/<category_id>")
def get_category(category_id):
    category = CategoryModel.query.get(category_id)
    if category:
        return category_schema.dump(category)
    return "Category not found", 404

@categories_bp.delete("/category/<category_id>")
def delete_category(category_id):
    category = CategoryModel.query.get(category_id)
    if category:
        RecordModel.query.filter_by(category_id=category_id).update({'category_id': None})
        db.session.commit()
        
        db.session.delete(category)
        db.session.commit()
        return category_schema.dump(category)
    return "Category not found", 404