"""Add Regions, Cities, Category hierarchy, favorites

Revision ID: f2b6a45d594a
Revises: 8fd8a3fb6720
Create Date: 2025-05-05 15:49:06.832692

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "f2b6a45d594a"
down_revision = "8fd8a3fb6720"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["categories.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "regions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email_address", sa.String(length=120), nullable=False),
        sa.Column("password_hash", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email_address"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "cities",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("region_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["region_id"],
            ["regions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("company", sa.String(length=200), nullable=False),
        sa.Column("url", sa.String(length=300), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("date_posted", sa.String(length=50), nullable=True),
        sa.Column("salary", sa.String(length=100), nullable=True),
        sa.Column("email", sa.String(length=120), nullable=True),
        sa.Column("city_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column(
            "date_populated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["categories.id"],
        ),
        sa.ForeignKeyConstraint(
            ["city_id"],
            ["cities.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url"),
    )
    op.create_table(
        "favorites",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("job_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["job_id"],
            ["jobs.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
    )
    op.drop_constraint("job_owner_user_id_fkey", "job", type_="foreignkey")
    op.drop_table("user")
    op.drop_table("job")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "job",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column(
            "location", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column(
            "company", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("url", sa.VARCHAR(length=200), autoincrement=False, nullable=False),
        sa.Column(
            "date_posted", sa.VARCHAR(length=20), autoincrement=False, nullable=False
        ),
        sa.Column("salary", sa.VARCHAR(length=50), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column("favorite", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("owner_user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            "date_populated",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "category", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"], ["user.id"], name="job_owner_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="job_pkey"),
        sa.UniqueConstraint("id", name="job_id_key"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "username", sa.VARCHAR(length=50), autoincrement=False, nullable=False
        ),
        sa.Column(
            "email_address", sa.VARCHAR(length=120), autoincrement=False, nullable=False
        ),
        sa.Column(
            "password_hash", sa.VARCHAR(length=128), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
        sa.UniqueConstraint("email_address", name="user_email_address_key"),
        sa.UniqueConstraint("id", name="user_id_key"),
        sa.UniqueConstraint("username", name="user_username_key"),
    )
    op.drop_table("favorites")
    op.drop_table("jobs")
    op.drop_table("cities")
    op.drop_table("users")
    op.drop_table("regions")
    op.drop_table("categories")
    # ### end Alembic commands ###
