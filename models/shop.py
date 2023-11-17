from typing import List

from sqlalchemy import String, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass


class Shop(Base):
    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    products: Mapped[List[int]] = mapped_column(ARRAY(Integer()))
    OOO: Mapped[str] = mapped_column(String(), nullable=False)
    # owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
