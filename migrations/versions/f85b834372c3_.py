"""empty message

Revision ID: f85b834372c3
Revises: 
Create Date: 2021-03-16 14:28:42.809248

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f85b834372c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resume_submissions',
    sa.Column('resume_submission_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('job_applied_to', mysql.TINYTEXT(), nullable=True),
    sa.Column('company_name', mysql.TINYTEXT(), nullable=True),
    sa.Column('contact_name_and_title', mysql.TINYTEXT(), nullable=True),
    sa.Column('phone', mysql.TINYTEXT(), nullable=True),
    sa.Column('email_and_other_contact', mysql.TINYTEXT(), nullable=True),
    sa.Column('mailing_address', mysql.TINYTEXT(), nullable=True),
    sa.Column('website', mysql.TINYTEXT(), nullable=True),
    sa.Column('date_resume_submitted', mysql.DATETIME(), nullable=True),
    sa.Column('date_cover_letter_submitted', mysql.DATETIME(), nullable=True),
    sa.Column('references_sent', mysql.TEXT(), nullable=True),
    sa.Column('method_of_discovery', mysql.TEXT(), nullable=True),
    sa.Column('job_description_and_keywords', mysql.TEXT(), nullable=True),
    sa.Column('status_of_application', mysql.TEXT(), nullable=True),
    sa.Column('comments', mysql.TEXT(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('resume_submission_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resume_submissions')
    # ### end Alembic commands ###
