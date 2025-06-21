from flask import Flask
from flask_migrate import Migrate  # ✅ import
from models import db
from routes import routes_app
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)  # ✅ initialize Flask-Migrate

app.register_blueprint(routes_app)
