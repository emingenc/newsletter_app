import re
from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY='dev',
        )
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app