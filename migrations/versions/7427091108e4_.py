"""empty message

Revision ID: 7427091108e4
Revises: 
Create Date: 2017-12-18 18:18:51.512100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7427091108e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('tab', sa.String(length=64), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('time_stamp', sa.DateTime(), nullable=False),
    sa.Column('time_last_modify', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_time_stamp'), 'post', ['time_stamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_index(op.f('ix_post_time_stamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
