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


    @classmethod
    def name_to_ids(cls):
        return { workspace.name: workspace.id for workspace in cls.query.all() }


    @classmethod
    def validate(cls, data):
        if len(data["name"]) < 4:
            return { "name": "Name must be at least 4 characters long" }, 400
        if cls.query.filter(cls.name == data["name"]).one_or_none():
            return { "name": "This name is alrady taken" }, 500
        return True


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id
        }


    def to_dict_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
