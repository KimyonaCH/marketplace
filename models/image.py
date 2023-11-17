from typing import List

from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass



class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    url_high: Mapped[str] = mapped_column(String(), nullable=False)
    url_mid:  Mapped[str] = mapped_column(String(), nullable=False)
    url_low: Mapped[str] = mapped_column(String(), nullable=False)