from datetime import datetime
from sqlalchemy.orm import validates
from .db import db


class Workspace(db.Model):
    __tablename__ = "workspaces"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    """ one-to-many """
    owner = db.relationship("User", back_populates="user_workspaces")
    channels = db.relationship("Channel", back_populates="workspace", cascade="all, delete-orphan")

    """ many-to-many """
    users = db.relationship('User', secondary="memberships", back_populates="workspaces")


    @validates('name')
    def validate_name(self, _, val):
        if len(val) < 4:
            raise ValueError({ "name": "Name must be at least 4 characters long" })
        return val


    @classmethod
    def name_to_ids(cls):
        return { workspace.name: workspace.id for workspace in cls.query.all() }
