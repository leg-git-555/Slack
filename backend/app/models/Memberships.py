from datetime import datetime
from .db import db


user_workspaces = db.Table(
  "pony_handlers",
  db.Model.metadata,
  user_id = db.Column(db.Integer, ForeignKey="users.id", primary_key=True),
  workspace_id = db.Column(db.Integer, ForeignKey="workspaces.id", primary_key=True),
  created_at = db.Column(db.Date, default=datetime.now),
  updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
)
