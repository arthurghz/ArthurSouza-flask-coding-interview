"""Add student and Course

Revision ID: c5be08b781f3
Revises: 1ddaa1d3a0b7
Create Date: 2025-01-07 13:43:46.311798

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c5be08b781f3'
down_revision = '1ddaa1d3a0b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "course",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("max_students", sa.Integer(), nullable=False),
        sa.Column("num_credits", sa.Integer(), nullable=False),
        sa.Column("professor_name", sa.String(), nullable=False)
    )

    op.create_table(
        "student",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("enrollment_date", sa.String(), nullable=False),
        sa.Column("min_courses_credits", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("user_id", sa.ForeignKey("users.id"), sa.Integer(), nullable=False),
        sa.Column("course_id",  sa.Integer(), nullable=True)
    )

    op.create_table(
        "enrollment",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("course_id", sa.Integer(), nullable=False),
        sa.Column("student_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint("course_id" , ["course.id"]),
        sa.ForeignKeyConstraint("student_id", ["student.id"]),
    )



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
