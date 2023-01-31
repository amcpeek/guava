"""adding teams- fixing users - redo db 

Revision ID: 70d3eea62afd
Revises: c669c3ce634b
Create Date: 2023-01-30 21:20:49.214390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70d3eea62afd'
down_revision = 'c669c3ce634b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teams', sa.Column('memberId', sa.Integer(), nullable=True))
    op.add_column('teams', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('teams', sa.Column('description', sa.String(length=255), nullable=False))
    op.drop_constraint(None, 'teams', type_='foreignkey')
    op.create_foreign_key(None, 'teams', 'users', ['memberId'], ['id'])
    op.drop_column('teams', 'userId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teams', sa.Column('userId', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'teams', type_='foreignkey')
    op.create_foreign_key(None, 'teams', 'users', ['userId'], ['id'])
    op.drop_column('teams', 'description')
    op.drop_column('teams', 'name')
    op.drop_column('teams', 'memberId')
    # ### end Alembic commands ###
