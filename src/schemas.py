from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=False)
    category_id = fields.Str(required=False)
    date = fields.DateTime(dump_only=True)
    expense = fields.Str(required=True)

class AccountSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=False)
    balance = fields.Str(dump_only=True)