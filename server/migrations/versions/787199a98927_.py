"""empty message

Revision ID: 787199a98927
Revises: d987afbcddd3
Create Date: 2021-03-18 11:46:18.511674

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '787199a98927'
down_revision = 'd987afbcddd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leads',
    sa.Column('lead_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lead_name_and_title', mysql.TINYTEXT(), nullable=True),
    sa.Column('company', mysql.TINYTEXT(), nullable=True),
    sa.Column('contact_information', mysql.TINYTEXT(), nullable=True),
    sa.Column('comments', mysql.TEXT(), nullable=True),
    sa.Column('created_at', mysql.TINYTEXT(), nullable=True),
    sa.Column('updated_at', mysql.TINYTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('lead_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leads')
    # ### end Alembic commands ###