from sqlalchemy.sql import text
from ..models import db, Channel


def seed_channels():
    channels = [
        {
            "name": "channel1",
            "owner_id": 1,
            "workspace_id": 1
        },
        {
            "name": "channel1",
            "owner_id": 1,
            "workspace_id": 2
        },
        {
            "name": "channel2",
            "owner_id": 1,
            "workspace_id": 2
        },

    ]

    for channel in channels:
        db.session.add(Channel(**channel))
        db.session.commit()


def undo_channels():
    db.session.execute(text("DELETE FROM channels"))
    db.session.commit()
