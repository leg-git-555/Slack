from datetime import datetime
from .db import db


class User(db.Model):

    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    profile_image_url = db.Column(db.String)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
