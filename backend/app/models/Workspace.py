from datetime import datetime
from .db import db


class Workspace(db.Model):

    __tablename__="workspaces"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False) #foreign key
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
