from datetime import datetime
from .db import db


class Message(db.Model):
    __tablename__ = "messages"


    id = db.Column(db.Integer, primary_key=True)
    is_private = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    workspace_id = db.Column(db.Integer, db.ForeignKey("workspaces.id"), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"))


    owner = db.relationship("User", back_populates="messages", foreign_keys=[sender_id])
    reactions = db.relationship("Reaction", back_populates="message", cascade="all, delete-orphan")
    channel = db.relationship("Channel", back_populates="messages")
