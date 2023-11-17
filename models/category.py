from typing import List

from sqlalchemy import String, Integer, ForeignKey, ARRAY
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass



class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)

