"""empty message

Revision ID: 016a6f59f8ee
Revises: 
Create Date: 2023-11-05 10:23:02.532219

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op
from common import StatusType

# revision identifiers, used by Alembic.
revision: str = "016a6f59f8ee"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("slug", sa.String, nullable=False, unique=True, index=True),
        sa.Column("status", sa.Enum(StatusType), nullable=False, index=True),
        sa.Column("priority", sa.Integer, nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("exec_date", sa.Date, nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            nullable=True,
            server_default=sa.func.now(),
            server_onupdate=sa.func.now(),
        ),
    )


def downgrade() -> None:
    op.drop_index(
        index_name="task_id_idx",
        table_name="tasks",
        if_exists=True,
    )
    op.drop_index(
        index_name="task_slug_idx",
        table_name="tasks",
        if_exists=True,
    )
    op.drop_index(
        index_name="task_status_idx",
        table_name="tasks",
        if_exists=True,
    )
    op.drop_table("tasks")
