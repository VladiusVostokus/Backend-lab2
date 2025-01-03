from flask import Flask
from users import users_bp
from categories import categories_bp
from records import records_bp
from flask_migrate import Migrate
from models import db, UserModel, CategoryModel, RecordModel, AccountModel

app = Flask(__name__)

app.config.from_pyfile('./config.py', silent=True)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(records_bp)
