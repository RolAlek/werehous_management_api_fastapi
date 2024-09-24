"""Create product table

Revision ID: 65f28d0ee821
Revises: 
Create Date: 2024-09-24 21:30:11.914551

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = "65f28d0ee821"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product",
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade() -> None:
    op.drop_table("product")
