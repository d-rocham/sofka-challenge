"""empty message

Revision ID: 72bd9c879bf0
Revises: b40acbef83ad
Create Date: 2022-04-04 18:43:57.982596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '72bd9c879bf0'
down_revision = 'b40acbef83ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('level_name', table_name='levels')
    op.drop_column('levels', 'level_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('levels', sa.Column('level_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=10), nullable=False))
    op.create_index('level_name', 'levels', ['level_name'], unique=False)
    # ### end Alembic commands ###
