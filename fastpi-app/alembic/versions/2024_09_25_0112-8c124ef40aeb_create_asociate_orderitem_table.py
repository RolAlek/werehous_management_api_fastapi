"""Create asociate OrderItem table

Revision ID: 8c124ef40aeb
Revises: 2c8f6a5f05cb
Create Date: 2024-09-25 01:12:53.078301

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "8c124ef40aeb"
down_revision: Union[str, None] = "2c8f6a5f05cb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "orderitem",
        sa.Column("order_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["order.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("orderitem")
