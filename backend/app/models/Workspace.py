from datetime import datetime
from .db import db


class Workspace(db.Model):
    __tablename__ = "workspaces"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    # owner = db.relationship("User", back_populates="user_workspaces")
    channels = db.relationship("Channel", back_populates="workspace", cascade="all, delete-orphan")
    users = db.relationship('User', secondary="user_workspaces", back_populates="workspaces")
