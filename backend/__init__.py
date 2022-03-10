import re
from flask import Flask
from backend.api.v1 import views

def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY='dev',
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(views.v1)

    return app