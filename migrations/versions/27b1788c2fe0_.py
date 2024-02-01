"""empty message

Revision ID: 27b1788c2fe0
Revises: 6f320e08a97a
Create Date: 2024-02-01 14:40:45.513902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27b1788c2fe0'
down_revision = '6f320e08a97a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('path_to_content', sa.String(length=100), nullable=True),
    sa.Column('diary_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conversation_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('user_type', sa.Enum('AI', 'user', 'system', name='conversation_user_type'), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('diary_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('path_to_content', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('conversation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('diary_entry')
    op.drop_table('conversation_message')
    op.drop_table('conversation')
    op.drop_table('user')
    # ### end Alembic commands ###
