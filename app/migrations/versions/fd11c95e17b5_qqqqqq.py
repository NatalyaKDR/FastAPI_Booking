"""qqqqqq

Revision ID: fd11c95e17b5
Revises: 82f221d395c3
Create Date: 2024-10-09 21:51:29.083177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd11c95e17b5'
down_revision: Union[str, None] = '82f221d395c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('otzivi', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hotels', 'otzivi')
    # ### end Alembic commands ###
