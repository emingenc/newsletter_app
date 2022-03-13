from flask.cli import FlaskGroup
from subprocess import call

from backend import create_app


cli = FlaskGroup(create_app=create_app)


if __name__ == "__main__":
    call('export FLASK_APP=backend', shell=True)
    create_app().run(host="0.0.0.0",port=8000 ,debug=True)