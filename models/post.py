from typing import List

from sqlalchemy import String, ForeignKey, Integer, Float, Boolean, ARRAY
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    address: Mapped[str] = mapped_column(String(), nullable=False)
    city: Mapped[str] = mapped_column(String(), nullable=False)
    working_time: Mapped[str] = mapped_column(String(), nullable=False)
    ratings: Mapped[float] = mapped_column(Float(), default=0.00)
    images: Mapped[List[int]] = mapped_column(ARRAY(Integer))
    storage: Mapped[bool] = mapped_column(Boolean(), default=False)
