"""created student and teacher tables

Revision ID: 87d614dbf1d3
Revises: 
Create Date: 2020-12-07 20:54:44.589555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87d614dbf1d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_fname', sa.Text(), nullable=True),
    sa.Column('student_lname', sa.Text(), nullable=True),
    sa.Column('student_email', sa.Text(), nullable=True),
    sa.Column('student_password', sa.Text(), nullable=True),
    sa.Column('student_attempted', sa.Integer(), nullable=True),
    sa.Column('student_solved', sa.Integer(), nullable=True),
    sa.Column('student_rank', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_fname', sa.Text(), nullable=True),
    sa.Column('teacher_lname', sa.Text(), nullable=True),
    sa.Column('teacher_email', sa.Text(), nullable=True),
    sa.Column('teacher_password', sa.Text(), nullable=True),
    sa.Column('teacher_rating', sa.Float(), nullable=True),
    sa.Column('teacher_no_Of_reviews', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    op.drop_table('students')
    # ### end Alembic commands ###