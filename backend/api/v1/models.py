from datetime import datetime
from backend.database import db


class Newsletter(db.Model):
    '''Newsletter model that contains news , 
    photo of news, title of news, and date of news'''
    __tablename__ = 'newsletters'
    id = db.Column(db.Integer, primary_key=True)
    news = db.Column(db.String(2500), nullable=False)
    photo = db.Column(db.String(400), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Newsletter %r>' % self.title
        
