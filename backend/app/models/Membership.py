from datetime import datetime
from .db import db


memberships = db.Table(
  "memberships",
  db.Column('user_id', db.Integer, db.ForeignKey("users.id"), primary_key=True),
  db.Column('workspace_id', db.Integer, db.ForeignKey("workspaces.id"), primary_key=True),
  db.Column('created_at', db.Date, default=datetime.now),
  db.Column('updated_at', db.Date, default=datetime.now, onupdate=datetime.now)
)
