"""create memerships table

Revision ID: 752e335fd76c
Revises: d943cf4f4c82
Create Date: 2024-02-13 16:28:49.508474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '752e335fd76c'
down_revision = 'd943cf4f4c82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memberships',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('workspace_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.Date(), nullable=True),
        sa.Column('updated_at', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'workspace_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memberships')
    # ### end Alembic commands ###
