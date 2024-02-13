from datetime import datetime
from .db import db


class Reaction(db.Model):

    __tablename__="reactions"

    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, nullable=False) #foreign key
    encoded_text = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
