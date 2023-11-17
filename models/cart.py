from typing import List

from sqlalchemy import Integer, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .base import Base

# class Base(DeclarativeBase):
#     pass


class Cart(Base):
    __tablename__ = "cart"

    id: Mapped[int] = mapped_column(primary_key=True)
    products_id: Mapped[List[int]] = mapped_column(ARRAY(Integer()))
