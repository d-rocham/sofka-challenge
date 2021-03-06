"""empty message

Revision ID: 67720836cc61
Revises: 3d9cea121ce6
Create Date: 2022-04-04 15:18:15.590110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67720836cc61'
down_revision = '3d9cea121ce6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level_id', sa.Integer(), nullable=False),
    sa.Column('question_text', sa.String(length=140), nullable=False),
    sa.ForeignKeyConstraint(['level_id'], ['levels.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_questions_level_id'), 'questions', ['level_id'], unique=False)
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('answer_text', sa.String(length=15), nullable=False),
    sa.Column('correct', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_answers_question_id'), 'answers', ['question_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_answers_question_id'), table_name='answers')
    op.drop_table('answers')
    op.drop_index(op.f('ix_questions_level_id'), table_name='questions')
    op.drop_table('questions')
    # ### end Alembic commands ###
