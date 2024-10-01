"""New Migr

Revision ID: 837c83081543
Revises: 7324b5396b18
Create Date: 2024-10-01 20:32:21.488381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '837c83081543'
down_revision: Union[str, None] = '7324b5396b18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
