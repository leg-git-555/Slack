from flask.cli import AppGroup
from .seed_users import seed_users
from .seed_workspaces import seed_workspaces
from .seed_channels import seed_channels


seed_cmd = AppGroup("seed")

@seed_cmd.command("all")
def seed_all():
  seed_users()
  seed_workspaces()
  seed_channels()
