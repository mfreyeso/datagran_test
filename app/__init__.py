from flask import Flask, request, current_app
from config import Config
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    db = MongoEngine(app)
    app.session_interface = MongoEngineSessionInterface(db)
    toolbar = DebugToolbarExtension(app)

    return app


from app import models
