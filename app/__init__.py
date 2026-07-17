from flask import Flask
from .database import init_database




def create_app():
    app = Flask(__name__, template_folder="templates")

    init_database()

    from .routes import main
    app.register_blueprint(main)

    return app