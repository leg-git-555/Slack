from datetime import datetime
from .db import db


class Message(db.Model):

    __tablename__="messages"

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer) # message_id
    sender_id = db.Column(db.Integer, nullable=False) #foreign key
    workspace_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    is_private = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
