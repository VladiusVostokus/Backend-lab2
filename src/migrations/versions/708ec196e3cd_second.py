"""Second

Revision ID: 708ec196e3cd
Revises: d45720df352f
Create Date: 2025-01-03 15:39:49.340261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '708ec196e3cd'
down_revision = 'd45720df352f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('expence',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('expence',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###