"""empty message

Revision ID: 02e1cad44361
Revises: a2967ac698e4
Create Date: 2021-01-28 10:54:57.417261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02e1cad44361'
down_revision = 'a2967ac698e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('modify_date', sa.DateTime(), nullable=True))
    op.add_column('question', sa.Column('modify_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'modify_date')
    op.drop_column('answer', 'modify_date')
    # ### end Alembic commands ###