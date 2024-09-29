"""Create new Order table.

Revision ID: 70c70f3fe4fe
Revises: 8e2f2b693e39
Create Date: 2024-09-29 18:26:45.258999

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "70c70f3fe4fe"
down_revision: Union[str, None] = "8e2f2b693e39"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "Собирается", "Доставляется", "Доставлен", name="orderstatus"
            ),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("orders")
