"""empty message

Revision ID: fcad4a457086
Revises: 78db01cd1fd0
Create Date: 2024-02-01 15:22:28.039479

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fcad4a457086'
down_revision = '78db01cd1fd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conversation', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('conversation_message', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'conversation', ['conversation_id'], ['id'])

    with op.batch_alter_table('diary_entry', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'conversation', ['conversation_id'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(collation='utf8_unicode_ci', length=100),
               type_=sa.String(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(collation='utf8_unicode_ci', length=100),
               existing_nullable=False)

    with op.batch_alter_table('diary_entry', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('conversation_message', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('conversation', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
