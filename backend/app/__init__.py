from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load Config
    app.config.from_object('config')

    # Register Blueprints (Routes)
    from .routes import main
    app.register_blueprint(main)

    return app
