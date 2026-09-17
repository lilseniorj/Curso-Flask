from flask import Flask

from auth.routes import auth_bp
from config import Config
from models import db
from notes.routes import notes_bp
from users.routes import users_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(notes_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)


    @app.route("/about")
    def about():
        return "This is a Notes app"

    return app

