from flask import Flask
from users import users_bp
from categories import categories_bp
from records import records_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(records_bp)

