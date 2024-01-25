"""comment

Revision ID: 02c707084417
Revises: c86fcc9d8dee
Create Date: 2023-12-06 16:24:52.410033

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "02c707084417"
down_revision = "c86fcc9d8dee"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("roles", postgresql.ARRAY(sa.String()), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "roles")
    # ### end Alembic commands ###
