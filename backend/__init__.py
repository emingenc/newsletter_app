import os
from flask import Flask
from backend.api.v1 import views
from backend.database import db
from flasgger import Swagger
from backend.config.swagger import template, swagger_config

def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )

    db.app = app
    db.init_app(app)    

    app.register_blueprint(views.v1)

    Swagger(app, config=swagger_config, template=template)

    return app
    