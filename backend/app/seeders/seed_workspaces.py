from sqlalchemy.sql import text
from ..models import db, Workspace


def seed_workspaces():
    workspaces = [
        {
            "name": "slack1",
            "owner_id": 1
        },
        {
            "name": "slack2",
            "owner_id": 1
        }
    ]

    for workspace in workspaces:
        db.session.add(Workspace(**workspace))
        db.session.commit()


def undo_workspaces():
    db.session.execute(text("DELETE FROM workspaces"))
    db.session.commit()
