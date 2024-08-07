"""added/removed columns from blogs table

Revision ID: 9d148feb3746
Revises: 
Create Date: 2024-07-05 19:54:29.051063

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9d148feb3746'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subtopic', sa.String(length=100), nullable=False))
        batch_op.alter_column('published',
               existing_type=mysql.DATETIME(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.drop_index('link')
        batch_op.drop_column('link')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', mysql.VARCHAR(length=100), nullable=False))
        batch_op.create_index('link', ['link'], unique=True)
        batch_op.alter_column('published',
               existing_type=mysql.DATETIME(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.drop_column('subtopic')

    # ### end Alembic commands ###
