from flask import Blueprint, request
from flask.json import jsonify


v1 = Blueprint("v1", __name__, url_prefix="/api/v1")

v1.route("/")(lambda: jsonify({"message": "Hello, World!"}))
