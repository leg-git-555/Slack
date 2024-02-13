from datetime import datetime
from .db import db


class Channel(db.Model):

    __tablename__="channels"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False) #foreign key
    workspace_id = db.Column(db.Integer, nullable=False) #foreign key
    name = db.Column(db.String(50), nullable=False) # unique for name and workspace combine
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
