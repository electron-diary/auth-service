"""empty message

Revision ID: c41d836f8130
Revises: 
Create Date: 2024-11-30 12:05:13.477883

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c41d836f8130"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("users",
    sa.Column("id", sa.UUID(), nullable=False),
    sa.Column("username", sa.String(), nullable=False),
    sa.Column("phone_number", sa.Integer(), nullable=False),
    sa.Column("is_deleted", sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("id"),
    sa.UniqueConstraint("phone_number"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
