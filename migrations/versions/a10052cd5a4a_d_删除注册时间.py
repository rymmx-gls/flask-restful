"""【D】删除注册时间

Revision ID: a10052cd5a4a
Revises: 13241b3d4bfb
Create Date: 2019-05-21 17:54:32.281991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10052cd5a4a'
down_revision = '13241b3d4bfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('register_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('register_time', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###
