"""empty message

Revision ID: 3d9cea121ce6
Revises: 
Create Date: 2022-04-04 15:13:47.714435

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3d9cea121ce6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('question_id', sa.Integer(), nullable=False))
    op.drop_index('ix_answers_level_id', table_name='answers')
    op.create_index(op.f('ix_answers_question_id'), 'answers', ['question_id'], unique=False)
    op.drop_constraint('answers_ibfk_1', 'answers', type_='foreignkey')
    op.create_foreign_key(None, 'answers', 'questions', ['question_id'], ['id'])
    op.drop_column('answers', 'level_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('level_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'answers', type_='foreignkey')
    op.create_foreign_key('answers_ibfk_1', 'answers', 'questions', ['level_id'], ['id'])
    op.drop_index(op.f('ix_answers_question_id'), table_name='answers')
    op.create_index('ix_answers_level_id', 'answers', ['level_id'], unique=False)
    op.drop_column('answers', 'question_id')
    # ### end Alembic commands ###
