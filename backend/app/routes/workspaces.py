from flask import Blueprint
from ..models import  Workspace

workspaces_bp = Blueprint("workspace", __name__, url_prefix="/workspaces")


@workspaces_bp.route("/")
def workspaces():
    workspaces = [workspace.to_dict() for workspace in Workspace.query.all()]
    return { "Workspaces": workspaces }


@workspaces_bp.route("/<int:id>")
def workspace(id):
    workspace = Workspace.query.get(id)

    if not workspace:
        return { "message": "Workspace couldn't be found" }, 404

    owner = workspace.owner.to_dict()
    members = [user.to_dict() for user in workspace.users]
    channels = [channel.to_dict() for channel in workspace.channels]

    return { **workspace.to_dict(), "Owner": owner, "Members": members, "Channels": channels }
