from flask import Blueprint, request
from flask.json import jsonify
from backend.api.v1.models import Newsletter
from backend.database import db
from flasgger import swag_from
from backend.constants.http_status_codes import (HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                                                 HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT)



v1 = Blueprint("v1", __name__, url_prefix="/api/v1")

v1.get("/ping")(lambda: jsonify({"message": "pong"}))


@v1.get("/newsletters")
@swag_from("docs/newsletters/stats.yaml")
def newsletters():
    newsletters = Newsletter.query.all()

    if newsletters:
        return jsonify({"newsletters": [newsletter.serialize() for newsletter in newsletters]})
    else:
        return jsonify({'message': 'Item not found'}), HTTP_404_NOT_FOUND



@v1.post("/newsletters")
@swag_from("docs/newsletters/stats.yaml")
def create_newsletter():
    data = request.get_json()
    newsletter = Newsletter(**data)
    db.session.add(newsletter)
    db.session.commit()

    return jsonify({"newsletter": newsletter.serialize()}) , HTTP_201_CREATED


@v1.get("/newsletters/<int:id>")
@swag_from("docs/newsletters/stats.yaml")
def newsletter(id):
    newsletter = Newsletter.query.get(id)

    return jsonify({"newsletter": newsletter.serialize()}) , HTTP_200_OK


@v1.put("/newsletters/<int:id>")
@swag_from("docs/newsletters/stats.yaml")
def update_newsletter(id):
    data = request.get_json()

    newsletter = Newsletter.query.get(id)
    newsletter.news = data["news"]
    newsletter.title = data["title"]
    newsletter.date = data["date"]

    db.session.commit()

    return jsonify({"newsletter": newsletter.serialize()}) , HTTP_200_OK

