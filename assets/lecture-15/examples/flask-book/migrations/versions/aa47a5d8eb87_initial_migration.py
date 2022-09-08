"""Initial migration

Revision ID: aa47a5d8eb87
Revises: 
Create Date: 2022-07-27 22:21:19.647690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa47a5d8eb87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=24), nullable=False),
    sa.Column('joined_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('friendships',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followee_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('follower_id', 'followee_id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_author_id'), 'post', ['author_id'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_author_id'), 'comment', ['author_id'], unique=False)
    op.create_index(op.f('ix_comment_post_id'), 'comment', ['post_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_post_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_author_id'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_post_author_id'), table_name='post')
    op.drop_table('post')
    op.drop_table('friendships')
    op.drop_table('user')
    # ### end Alembic commands ###
