from typing import List

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
# from .base import Base


class Base(DeclarativeBase):
    pass


class Subcategory(Base):
    __tablename__ = "subcategory"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey("category.id"))
