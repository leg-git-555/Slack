from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from ..models import  db, Workspace

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


@workspaces_bp.route("/", methods=["POST"])
def create_workspace():
    data = request.json
    result = Workspace.validate(data)

    if (result != True):
        return result

    new_workspace = Workspace(**data)
    db.session.add(new_workspace)
    db.session.commit()

    return new_workspace.to_dict(), 201


@workspaces_bp.route("/", methods=["PUT"])
def update_workspace():
    pass


@workspaces_bp.route("/", methods=["DELETE"])
def delete_workspace():
    pass
