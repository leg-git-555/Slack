from flask.cli import AppGroup
from .seed_users import seed_users, undo_users
from .seed_workspaces import seed_workspaces, undo_workspaces
from .seed_channels import seed_channels, undo_channels


seed_cmd = AppGroup("seed")

@seed_cmd.command("all")
def seed_all():
  seed_users()
  seed_workspaces()
  seed_channels()

@seed_cmd.command("undo")
def seed_undo():
  undo_channels()
  undo_workspaces()
  undo_users()
