from flask import Flask
from flask_migrate import Migrate
# from .seeders import seed_cmd
from .models import db
from .routes import main
from .config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(main.bp)
db.init_app(app)
Migrate(app, db)
# app.cli.add_command(seed_cmd)
