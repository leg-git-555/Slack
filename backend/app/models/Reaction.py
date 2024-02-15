from datetime import datetime
from .db import db


class Reaction(db.Model):
    __tablename__="reactions"


    id = db.Column(db.Integer, primary_key=True)
    encoded_text = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey("messages.id"), nullable=False)


    """ one-to-many """
    message = db.relationship("Message", back_populates="reactions")
    user = db.relationship("User", back_populates="reactions")
