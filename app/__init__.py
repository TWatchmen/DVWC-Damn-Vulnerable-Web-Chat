

from flask import Flask
from .database import init_database

SECRET_KEY = "Secret Key"



def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SECRET_KEY"] = SECRET_KEY

    init_database()

    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app