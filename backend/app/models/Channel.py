from datetime import datetime
from sqlalchemy.orm import validates
from .db import db


class Channel(db.Model):
    __tablename__ = "channels"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    workspace_id = db.Column(db.Integer, db.ForeignKey("workspaces.id"), nullable=False)


    owner = db.relationship("User", back_populates="channels")
    workspace = db.relationship("Workspace", back_populates="channels")
    messages = db.relationship("Message", back_populates="channel", cascade="all, delete-orphan")


    @validates('name')
    def validate_name(self, _, val):
        if len(val) < 4:
            raise ValueError({"message": "Name must be at least 4 characters long"})
        return val
