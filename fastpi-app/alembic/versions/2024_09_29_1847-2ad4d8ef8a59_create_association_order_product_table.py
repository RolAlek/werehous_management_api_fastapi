"""Create association order_product table

Revision ID: 2ad4d8ef8a59
Revises: 70c70f3fe4fe
Create Date: 2024-09-29 18:47:31.053965

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "2ad4d8ef8a59"
down_revision: Union[str, None] = "70c70f3fe4fe"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product_order_association",
        sa.Column("order_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column(
            "count_in_cart", sa.Integer(), server_default="1", nullable=False
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["orders.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "order_id", "product_id", name="idx_unique_order_product"
        ),
    )


def downgrade() -> None:
    op.drop_table("product_order_association")
