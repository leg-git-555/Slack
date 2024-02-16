from flask import Blueprint
from .workspaces import workspaces_bp
from .channels import channels_bp


api_bp = Blueprint("api", __name__, url_prefix="/api")
workspaces = api_bp.register_blueprint(workspaces_bp)
channels = api_bp.register_blueprint(channels_bp)
