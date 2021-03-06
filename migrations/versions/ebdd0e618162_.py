"""empty message

Revision ID: ebdd0e618162
Revises: 364445d0e729
Create Date: 2021-01-28 10:01:07.906056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebdd0e618162'
down_revision = '364445d0e729'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    # ### end Alembic commands ###
