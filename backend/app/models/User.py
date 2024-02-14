from datetime import datetime
from .db import db


class User(db.Model):
    __tablename__ = "users"


    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    hashed_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    profile_image_url = db.Column(db.String)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)


    user_workspaces = db.relationship("Workspace", back_populates="owner", cascade="all, delete-orphan")
    channels = db.relationship("Channel", back_populates="owner")
    messages = db.relationship("Message", back_populates="owner")
    reactions = db.relationship("Reaction", back_populates="user")
    workspaces = db.relationship('Workspace', secondary="user_workspaces", back_populates="users")
