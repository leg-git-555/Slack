from sqlalchemy.sql import text
from ..models import db, User

def seed_users():
    users = [
        {
            "first_name": "Hao",
            "last_name": "Lam",
            "username": "haolam",
            "hashed_password": "password",
            "email": "haolam@user.io"
        },
        {
            "first_name": "Nicky",
            "last_name": "Lei",
            "username": "nickylei",
            "hashed_password": "password2",
            "email": "nickylei@user.io"
        },
        {
            "first_name": "Nick",
            "last_name": "Leger",
            "username": "nickleger",
            "hashed_password": "password3",
            "email": "nickleger@user.io"
        },
        {
            "first_name": "Luffy",
            "last_name": "Monkey D.",
            "username": "luffy",
            "hashed_password": "password4",
            "email": "luffy@user.io"

        },
        {
            "first_name": "Zoro",
            "last_name": "Roronoa",
            "username": "zoro",
            "hashed_password": "password5",
            "email": "zoro@user.io"
        },
        {
            "first_name": "Sanji",
            "last_name": "Vinsmoke",
            "username": "sanji",
            "hashed_password": "password6",
            "email": "sanji@user.io"
        },
                {
            "first_name": "Robin",
            "last_name": "Nico",
            "username": "Robin",
            "hashed_password": "password7",
            "email": "robin@user.io"

        },
        {
            "first_name": "Mihawk",
            "last_name": "Dracule",
            "username": "Mihawk",
            "hashed_password": "password8",
            "email": "mihawk@user.io"
        },
        {
            "first_name": "Ace",
            "last_name": "Portgas D.",
            "username": "Acee",
            "hashed_password": "password9",
            "email": "ace@user.io"
        }
    ]

    for user in users:
        db.session.add(User(**user))
        db.session.commit()

def undo_users():
    db.session.execute(text("DELETE FROM users"))
    db.session.commit()
