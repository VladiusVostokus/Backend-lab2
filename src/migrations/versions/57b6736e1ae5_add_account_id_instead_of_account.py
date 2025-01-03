"""Add account id instead of account

Revision ID: 57b6736e1ae5
Revises: 68a85487d62a
Create Date: 2025-01-03 21:18:55.472719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57b6736e1ae5'
down_revision = '68a85487d62a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_id', sa.UUID(), nullable=False))
        batch_op.create_unique_constraint(None, ['account_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('account_id')

    # ### end Alembic commands ###
