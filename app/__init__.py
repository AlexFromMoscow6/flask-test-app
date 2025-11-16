from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv("SECRET_KEY")

    from .routes import main
    app.register_blueprint(main)

    return app
