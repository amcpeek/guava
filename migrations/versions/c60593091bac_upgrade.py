"""upgrade

Revision ID: c60593091bac
Revises: b88679e83d26
Create Date: 2023-01-31 13:33:38.195868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c60593091bac'
down_revision = 'b88679e83d26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('assigneeId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'users', ['assigneeId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'assigneeId')
    # ### end Alembic commands ###
