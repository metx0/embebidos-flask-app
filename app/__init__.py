from flask import Flask


def create_app():
    app = Flask(__name__)

    # Registrar los blueprints
    from .api import api
    from .vistas import vistas

    app.register_blueprint(api, url_prefix="/")
    app.register_blueprint(vistas, url_prefix="/")

    @app.route("/bienvenida")
    def saludar():
        return "Bienvenido al servidor"

    @app.route("/hello")
    def hello():
        return "Hello world!"

    return app
