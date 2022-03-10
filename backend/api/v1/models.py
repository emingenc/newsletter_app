import string
import random
from datetime import datetime
from backend.database import db


class Newsletter(db.Model):
    '''Newsletter model that contains news , 
    photo of news, title of news, and date of news'''
    __tablename__ = 'newsletters'
    id = db.Column(db.Integer, primary_key=True)
    news = db.Column(db.String(2500), nullable=False)
    photo = db.Column(db.LargeBinary)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def generate_short_characters(self):
        characters = string.digits+string.ascii_letters
        picked_chars = ''.join(random.choices(characters, k=3))

        link = self.query.filter_by(short_url=picked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return picked_chars

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url = self.generate_short_characters()

    def __repr__(self):
        return '<Newsletter %r>' % self.title
        