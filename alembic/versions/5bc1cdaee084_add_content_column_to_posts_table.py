"""add content column to posts table

Revision ID: 5bc1cdaee084
Revises: 1dae4350e2c4
Create Date: 2024-04-26 16:21:00.004060

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5bc1cdaee084"
down_revision: Union[str, None] = "1dae4350e2c4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
