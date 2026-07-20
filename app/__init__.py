from flask import Flask
from .database import init_database




def create_app():
    app = Flask(__name__, template_folder="templates")

    init_database()

    from .routes import vuln
    app.register_blueprint(vuln)

    return app