from sqlalchemy.sql import text
from ..models import db, User, Channel, Message


def seed_messages():
    username_to_ids = User.username_to_ids()
    c_w_to_ids = Channel.channel_and_workspace_name_to_ids()

    messages = [
       {
          "is_private": True,
          "message": "Hi, my name is Hao",
          "sender_id": username_to_ids["haolam"],
          "receiver_id": username_to_ids["nickleger"]
       },
       {
          "is_private": True,
          "message": "Nice to meet you 😀",
          "sender_id": username_to_ids["haolam"],
          "receiver_id": username_to_ids["nickleger"]
       },
       {
          "is_private": True,
          "message": "Do I know you???",
          "sender_id": username_to_ids["nickleger"],
          "receiver_id": username_to_ids["haolam"]
       },
       {
          "is_private": False,
          "message": "Hey guys, let's start by introduce ourselves...",
          "sender_id": username_to_ids["haolam"],
          "channel_id": c_w_to_ids["general:hao-nick-nicky"]
       },
       {
          "is_private": False,
          "message": "My name is Nicky.",
          "sender_id": username_to_ids["nickylei"],
          "channel_id": c_w_to_ids["general:hao-nick-nicky"]
       },
       {
          "is_private": False,
          "message": "I'm Nick",
          "sender_id": username_to_ids["nickleger"],
          "channel_id": c_w_to_ids["general:hao-nick-nicky"]
       },
    ]

    [db.session.add(Message(**message)) for message in messages]
    db.session.commit()


def undo_messages():
  db.session.execute(text("DELETE FROM messages"))
  db.session.commit()
