"""empty message

Revision ID: fc0b52c4f842
Revises: 713af9635f46
Create Date: 2018-07-15 16:32:56.363053

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'fc0b52c4f842'
down_revision = '713af9635f46'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_emails',
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_address', sa.String(length=120), nullable=False),
    sa.Column('type', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_emails')
    # ### end Alembic commands ###
