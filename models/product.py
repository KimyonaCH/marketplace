from typing import List

from sqlalchemy import String, ForeignKey, Integer, CheckConstraint, Float, ARRAY
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    price: Mapped[int] = mapped_column(Integer(), nullable=False)
    discount: Mapped[int] = mapped_column(Integer(), default=0)
    description: Mapped[str] = mapped_column(String())
    ratings: Mapped[float] = mapped_column(Float(), default=0.00)
    brand: Mapped[str] = mapped_column(String(), nullable=False)
    images: Mapped[List[int]] = mapped_column(ARRAY(Integer))
    features_id: Mapped[List[int]] = mapped_column(ARRAY(Integer))
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey("category.id"))
    # shop_id: Mapped[int] = mapped_column(Integer(), ForeignKey("shop.id"))

    __table_args__ = (
        CheckConstraint("discount >= 0 and discount <= 100", name="discount_range"),
    )
