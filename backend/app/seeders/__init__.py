from flask.cli import AppGroup
from .seed_users import seed_users


seed_cmd = AppGroup("seed")

@seed_cmd.command("all")
def seed_all():
  seed_users()
