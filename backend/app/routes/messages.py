from flask import Blueprint
from ..models import  Message

messages_bp = Blueprint("message", __name__, url_prefix="/messages")


@messages_bp.route("/")
def messages():
    messages = [message.to_dict() for message in Message.query.all()]
    return { "messages": messages }


@messages_bp.route("/<int:id>")
def message(id):
    message = Message.query.get(id)

    if not message:
        return { "message": "Message couldn't be found" }, 404

    owner = message.owner.to_dict()
    channel = message.channel.to_dict() if message.channel else None
    reactions = [reaction.to_dict() for reaction in message.reactions]

    return { **message.to_dict(), "Owner": owner, "Channel": channel, "Reactions": reactions }
