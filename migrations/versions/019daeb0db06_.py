"""empty message

Revision ID: 019daeb0db06
Revises: 13dd3914e8d9
Create Date: 2022-06-28 17:37:20.618603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019daeb0db06'
down_revision = '13dd3914e8d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=120), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###