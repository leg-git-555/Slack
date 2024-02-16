from datetime import datetime
from sqlalchemy.orm import validates
from .db import db


class Reaction(db.Model):
    __tablename__="reactions"


    id = db.Column(db.Integer, primary_key=True)
    encoded_text = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey("messages.id"), nullable=False)


    """ one-to-many """
    message = db.relationship("Message", back_populates="reactions")
    user = db.relationship("User", back_populates="reactions")


    @validates('encoded_text')
    def validate_message(self, _, val):
        if not len(val):
            raise ValueError({ "encoded_text": "Reaction is required" })
        return val


    def to_dict(self):
        return {
            "id": self.id,
            "encoded_text": self.encoded_text,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "message_id": self.message_id
        }
