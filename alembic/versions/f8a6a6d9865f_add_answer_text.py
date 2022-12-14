"""add answer text

Revision ID: f8a6a6d9865f
Revises: 3adad33e0907
Create Date: 2022-10-04 19:26:15.308292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8a6a6d9865f'
down_revision = '3adad33e0907'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('answer', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'answer')
    # ### end Alembic commands ###
