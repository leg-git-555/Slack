from flask import Blueprint

workspaces_bp = Blueprint("workspace", __name__, url_prefix="/workspaces")


@workspaces_bp.route("/")
def workspaces():
  return "All workspaces"
