from sqlalchemy.sql import text
from ..models import db, Workspace, User


def seed_workspaces():
    username_to_ids = User.username_to_ids()

    workspaces = [
        {
            "name": "aA Union",
            "owner_id": username_to_ids["haolam"]
        },
        {
            "name": "hao-nick-nicky",
            "owner_id": username_to_ids["haolam"]
        },
        {
            "name": "hao-nick",
            "owner_id": username_to_ids["haolam"]
        },
        {
            "name": "hao-nicky",
            "owner_id": username_to_ids["haolam"]
        },
        {
            "name": "nick-nicky",
            "owner_id": username_to_ids["haolam"]
        }
    ]

    for workspace in workspaces:
        db.session.add(Workspace(**workspace))
        db.session.commit()


def undo_workspaces():
    db.session.execute(text("DELETE FROM workspaces"))
    db.session.commit()
