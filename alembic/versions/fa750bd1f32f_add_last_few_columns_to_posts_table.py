"""add last  few columns to posts table

Revision ID: fa750bd1f32f
Revises: da3b09de4c76
Create Date: 2024-04-27 15:47:20.840954

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fa750bd1f32f"
down_revision: Union[str, None] = "da3b09de4c76"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean, nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "create_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
