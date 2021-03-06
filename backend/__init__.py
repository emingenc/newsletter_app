import os
from flask import Flask
from backend.api.v1.views import v1
from backend.auth.views import auth
from backend.database import db
from flasgger import Swagger
from backend.config.swagger import template, swagger_config
from flask_jwt_extended import JWTManager
from flask_cors import CORS
dbuser = os.environ.get('POSTGRES_USERNAME')
dbpass = os.environ.get('POSTGRES_PASSWORD')
dbhost = os.environ.get('POSTGIS_HOSTNAME')
dbname = os.environ.get('DBNAME')

def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True,
                static_url_path='', 
                static_folder='static',)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=f'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}',
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),


            SWAGGER={
                'title': "Bookmarks API",
                'uiversion': 3
            }
        )

    db.app = app
    db.init_app(app)    

    JWTManager(app)
    app.register_blueprint(v1)
    app.register_blueprint(auth)

    @app.before_first_request
    def create_tables():
        db.create_all()
    

    Swagger(app, config=swagger_config, template=template)
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    return app
    