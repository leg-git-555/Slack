from flask import Blueprint
from ..models import  Channel

channels_bp = Blueprint("channel", __name__, url_prefix="/channels")


@channels_bp.route("/")
def channels():
    channels = [channel.to_dict() for channel in Channel.query.all()]
    return { "channels": channels }


@channels_bp.route("/<int:id>")
def channel(id):
    channel = Channel.query.get(id)

    if not channel:
        return { "message": "Channel couldn't be found" }, 404

    owner = channel.owner.to_dict()
    workspace = channel.workspace.to_dict()
    messages = [message.to_dict() for message in channel.messages]

    return { **channel.to_dict(), "Owner": owner, "Workspace": workspace, "Messages": messages }
