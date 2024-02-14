from datetime import datetime
from .db import db


class Channel(db.Model):
    __tablename__ = "channels"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    workspace_id = db.Column(db.Integer, db.ForeignKey("workspaces.id"), nullable=False)

    c_index = db.UniqueConstraint('name', 'workspace_id') # define unique constraint for name and workspace_id combination


    owner = db.relationship("User", back_populates="channels")
    workspace = db.relationship("Workspace", back_populates="channels")
    messages = db.relationship("Message", back_populates="channel", cascade="all, delete-orphan")
