from flask import Flask

from api.config import configs


def create_app(config=None):
    app = Flask(__name__)

    # set the configuration using the FLASK_ENV environment variable if
    # config not provided
    app.config.from_object(config or configs[app.env])

    return app
