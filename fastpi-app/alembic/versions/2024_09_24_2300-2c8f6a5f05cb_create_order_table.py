"""Create order table

Revision ID: 2c8f6a5f05cb
Revises: 65f28d0ee821
Create Date: 2024-09-24 23:00:26.777834

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = "2c8f6a5f05cb"
down_revision: Union[str, None] = "65f28d0ee821"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "order",
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("Собирается", "Доставляется", "Доставлен", name="orderstatus"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("order")
