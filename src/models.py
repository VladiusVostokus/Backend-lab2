from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.UUID(),primary_key=True)
    name = db.Column(db.String(64), unique = True, nullable = False)
    account_id = db.Column(db.UUID(), unique = True, nullable = False)
    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")
    account = db.relationship("AccountModel", back_populates="user")

class CategoryModel(db.Model):
    __tablename__ = "category"
    id = db.Column(db.UUID(),primary_key = True)
    name = db.Column(db.String(64), unique = True, nullable = False)

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")

class RecordModel(db.Model):
    __tablename__ = "record"
    id = db.Column(db.UUID(),primary_key = True)
    user_id = db.Column(db.UUID(), db.ForeignKey("user.id", ondelete = 'SET NULL'), unique = False, nullable = True)
    category_id = db.Column(db.UUID(),db.ForeignKey('category.id', ondelete = 'SET NULL'), unique = False, nullable = True)
    date = db.Column(db.TIMESTAMP, server_default=func.now())
    expense = db.Column(db.String(64), unique = False, nullable = False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")

class AccountModel(db.Model):
    __tablename__ = "account"
    id = db.Column(db.UUID(),primary_key = True)
    user_id = db.Column(db.UUID(), db.ForeignKey("user.id"), unique = False, nullable = False)
    balance = db.Column(db.String(64), unique = False, nullable = False)

    user = db.relationship("UserModel", back_populates="account")