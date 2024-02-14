from passlib.hash import sha256_crypt
from ..models import db, User

def seed_users():
    users = [
        {
            "first_name": "Hao",
            "last_name": "Lam",
            "username": "haolam",
            "hashed_password": sha256_crypt.encrypt("password"),
            "email": "haolam@user.io",
            
        },
        {
            "first_name": "Nicky",
            "last_name": "Lei",
            "username": "nickylei",
            "hashed_password": sha256_crypt.encrypt("password1"),
            "email": "nickylei@user.io",
        },
        {
            "first_name": "Nick",
            "last_name": "Leger",
            "username": "nickleger",
            "hashed_password": sha256_crypt.encrypt("password2"),
            "email": "nickleger@user.io",
        }
    ]

    for user in users:
        db.session.add(User(**user))
        db.session.commit()