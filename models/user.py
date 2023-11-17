from datetime import date
from typing import List

from sqlalchemy import String, ForeignKey, Integer, Date, ARRAY
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base


# class Base(DeclarativeBase):
#     pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(String(), nullable=False)
    email: Mapped[str] = mapped_column(String(), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date())
    city: Mapped[str] = mapped_column(String())
    favourite: Mapped[List[int]] = mapped_column(ARRAY(Integer()))
    cart_id: Mapped[int] = mapped_column(Integer(), ForeignKey("cart.id"), nullable=True)
    purchase_history: Mapped[List[int]] = mapped_column(ARRAY(Integer))
