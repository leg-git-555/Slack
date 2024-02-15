from flask.cli import AppGroup
from .seed_users import seed_users, undo_users
from .seed_workspaces import seed_workspaces, undo_workspaces
from .seed_channels import seed_channels, undo_channels
from .seed_membership import seed_memberships, undo_memberships

seed_cmd = AppGroup("seed")


@seed_cmd.command("all")
def seed_all():
  seed_all_tables()


@seed_cmd.command("undo")
def seed_undo():
  unseed_all_tables()


@seed_cmd.command("reset")
def seed_reset():
  unseed_all_tables()
  seed_all_tables()


def seed_all_tables():
  seed_users()
  seed_workspaces()
  seed_channels()
  seed_memberships()


def unseed_all_tables():
  undo_memberships()
  undo_channels()
  undo_workspaces()
  undo_users()
