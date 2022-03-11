import os
import uuid
from flask import  Blueprint, request
from flask.json import jsonify
from backend.api.v1.models import Newsletter, db
from flasgger import swag_from
from pathlib import Path
from flask_jwt_extended import jwt_required
from backend.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND


v1 = Blueprint("v1", __name__, url_prefix="/api/v1")

v1.get("/ping")(lambda: jsonify({"message": "pong"}))


@v1.get("/newsletters")
@swag_from("docs/newsletters.yaml")
def newsletters():
    newsletters = Newsletter.query.all()

    if newsletters:
        return jsonify({"newsletters": [{ "id": newsletter.id,
                                            "news": newsletter.news,
                                            "title": newsletter.title,
                                            "photo": newsletter.photo,
                                            "date": newsletter.date,
                                            "updated_at": newsletter.updated_at} for newsletter in newsletters]})
    else:
        return jsonify({'message': 'Item not found'}), HTTP_404_NOT_FOUND



@v1.post("/newsletters")
@jwt_required()
@swag_from("docs/newsletters.yaml")
def create_newsletter():
    # form data
    data = request.form
    news = data.get("news")
    title = data.get("title")
    file = request.files.get("photo")
    name = str(uuid.uuid4()).split('-')[0]
    ext = file.filename.split('.')[-1]
    photo = f'{os.environ.get("UPLOAD_FOLDER")}{ name}.{ext}'
    photo_name = f'uploads/{name}.{ext}'
    file.save(photo)

    newsletter = Newsletter(news = news, title = title, photo = photo_name)
    db.session.add(newsletter)
    db.session.commit()

    return jsonify({
        "message": "Newsletter created successfully",
        "id": newsletter.id,
        "news": newsletter.news,
        "title": newsletter.title,
        "photo": newsletter.photo,
        "date": newsletter.date
    }) , HTTP_201_CREATED


@v1.get("/newsletters/<int:id>")
@swag_from("docs/newsletters_detailed.yaml")
def newsletter(id):
    newsletter = Newsletter.query.get(id)

    return jsonify({
        "id": newsletter.id,
        "news": newsletter.news,
        "title": newsletter.title,
        "photo": newsletter.photo,
        "date": newsletter.date,
        "updated_at": newsletter.updated_at
    }) , HTTP_200_OK


@v1.put("/newsletters/<int:id>")
@jwt_required()
@swag_from("docs/newsletters_detailed.yaml")
def update_newsletter(id):
    data = request.form

    newsletter = Newsletter.query.get(id)
    newsletter.news = data["news"]
    newsletter.title = data["title"]
    file = request.files.get("photo")

    if file:
        print(newsletter.photo,'sddsad')
        old_photo = Path.cwd() / 'backend/static'/newsletter.photo
        print(old_photo)
        if old_photo.exists():
            print(f"Deleting {newsletter.photo}")
            os.remove(old_photo)
        name = str(uuid.uuid4()).split('-')[0]
        ext = file.filename.split('.')[-1]
        photo = f'{os.environ.get("UPLOAD_FOLDER")}{ name}.{ext}'
        file.save(photo)
        photo_name = f'uploads/{name}.{ext}'
        newsletter.photo = photo_name

    db.session.commit()

    return jsonify({
        "message": "Newsletter updated successfully",
        "id": newsletter.id,
        "news": newsletter.news,
        "title": newsletter.title,
        "photo": newsletter.photo,
        "date": newsletter.date
    }) , HTTP_200_OK

