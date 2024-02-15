from datetime import datetime
from sqlalchemy.orm import validates
from .db import db


class Message(db.Model):
    __tablename__ = "messages"


    id = db.Column(db.Integer, primary_key=True)
    is_private = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"))


    """ one-to-many """
    owner = db.relationship("User", back_populates="messages", foreign_keys=[sender_id])
    reactions = db.relationship("Reaction", back_populates="message", cascade="all, delete-orphan")
    channel = db.relationship("Channel", back_populates="messages")


    @validates('message')
    def validate_message(self, _, val):
        if not len(val):
            raise ValueError({ "message": "Message is required" })
        return val
