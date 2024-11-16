from flask import Flask


def create_app():
    app = Flask(__name__)

    # Registrar los blueprints
    from .api import api

    app.register_blueprint(api, url_prefix="/")

    @app.route("/")
    def saludar():
        return "Bienvenido al servidor"

    @app.route("/hello")
    def hello():
        return "Hello world!"

    return app
