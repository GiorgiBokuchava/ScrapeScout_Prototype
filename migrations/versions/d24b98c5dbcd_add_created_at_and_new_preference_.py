"""Add created_at and new preference columns to user

Revision ID: d24b98c5dbcd
Revises: bf01a918e901
Create Date: 2025-05-12 16:54:32.477344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd24b98c5dbcd'
down_revision = 'bf01a918e901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('saved_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('saved_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('viewed_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('viewed_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_job_category_key'), ['category_key'], unique=False)
        batch_op.create_index(batch_op.f('ix_job_location_key'), ['location_key'], unique=False)
        batch_op.create_unique_constraint(None, ['url'])
        batch_op.drop_constraint('job_owner_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('favorite')
        batch_op.drop_column('owner_user_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('theme', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('font_size', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('default_location', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('jobs_per_page', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('sort_order', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('profile_visible', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('activity_visible', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('data_collection_enabled', sa.Boolean(), nullable=True))
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=30),
               existing_nullable=False)
        batch_op.alter_column('email_address',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
        batch_op.alter_column('email_address',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=30),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
        batch_op.drop_column('data_collection_enabled')
        batch_op.drop_column('activity_visible')
        batch_op.drop_column('profile_visible')
        batch_op.drop_column('sort_order')
        batch_op.drop_column('jobs_per_page')
        batch_op.drop_column('default_location')
        batch_op.drop_column('font_size')
        batch_op.drop_column('theme')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('favorite', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('job_owner_user_id_fkey', 'user', ['owner_user_id'], ['id'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_index(batch_op.f('ix_job_location_key'))
        batch_op.drop_index(batch_op.f('ix_job_category_key'))

    op.drop_table('viewed_job')
    op.drop_table('saved_job')
    # ### end Alembic commands ###
