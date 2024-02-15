from datetime import datetime
from passlib.hash import sha256_crypt
from sqlalchemy.orm import validates
from .db import db
from .Message import Message


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
    messages = db.relationship("Message", back_populates="owner", foreign_keys=[Message.sender_id])
    reactions = db.relationship("Reaction", back_populates="user")
    workspaces = db.relationship('Workspace', secondary="user_workspaces", back_populates="users")


    @validates('username')
    def validate_username(self, _, val):
        if len(val) < 4:
            raise ValueError({"message": "Username must be at least 4 characters long"})
        return val


    @validates('hashed_password')
    def validate_hashed_password(self, _, val):
        if len(val) < 6:
            raise ValueError({"message": "Password must be at least 6 characters long"})
        return sha256_crypt.hash(val)


    @validates("email")
    def validate_email(self, _, val):
        if "@" not in val:
            raise ValueError({"message": "Invalid email"})
        return val
