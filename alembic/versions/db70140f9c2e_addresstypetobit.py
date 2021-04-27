"""AddressTypeToBit

Revision ID: db70140f9c2e
Revises: 4a3940c13997
Create Date: 2021-04-27 18:19:11.436967

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'db70140f9c2e'
down_revision = '4a3940c13997'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token_snapshots', sa.Column('is_contract', mysql.BIT(), nullable=True))
    op.drop_column('token_snapshots', 'address_type')
    op.add_column('transfer_info', sa.Column('is_contract', mysql.BIT(), nullable=False))
    op.drop_column('transfer_info', 'address_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transfer_info', sa.Column('address_type', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('transfer_info', 'is_contract')
    op.add_column('token_snapshots', sa.Column('address_type', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('token_snapshots', 'is_contract')
    # ### end Alembic commands ###