"""add avaliable task

Revision ID: ab99bff75efe
Revises: f8a6a6d9865f
Create Date: 2022-10-04 20:12:12.727159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab99bff75efe'
down_revision = 'f8a6a6d9865f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('avaliable_task', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'avaliable_task')
    # ### end Alembic commands ###