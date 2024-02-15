from sqlalchemy.sql import text
from ..models import db, Workspace


def seed_workspaces():
    workspaces = [
        {
            "name": "aA Union",
            "owner_id": 1
        },
        {
            "name": "hao-nick-nicky",
            "owner_id": 1
        },
        {
            "name": "hao-nick",
            "owner_id": 1
        },
        {
            "name": "hao-nicky",
            "owner_id": 1
        },
        {
            "name": "nick-nicky",
            "owner_id": 1
        }
    ]

    for workspace in workspaces:
        db.session.add(Workspace(**workspace))
        db.session.commit()


def undo_workspaces():
    db.session.execute(text("DELETE FROM workspaces"))
    db.session.commit()
