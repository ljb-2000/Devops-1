"""empty message

Revision ID: 05994d747975
Revises: 968c5bad1e86
Create Date: 2016-01-25 11:25:00.041630

"""

# revision identifiers, used by Alembic.
revision = '05994d747975'
down_revision = '968c5bad1e86'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('uuid', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('server', 'uuid')
    ### end Alembic commands ###
