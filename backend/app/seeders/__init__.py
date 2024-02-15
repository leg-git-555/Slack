from flask.cli import AppGroup
from .seed_users import seed_users, undo_users
from .seed_workspaces import seed_workspaces, undo_workspaces
from .seed_channels import seed_channels, undo_channels
from .seed_memberships import seed_memberships, undo_memberships
from .seed_messages import seed_messages, undo_messages
from .seed_reactions import seed_reactions, undo_reactions

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
  seed_messages()
  seed_reactions()


def unseed_all_tables():
  undo_reactions()
  undo_messages()
  undo_memberships()
  undo_channels()
  undo_workspaces()
  undo_users()
