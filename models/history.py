from datetime import datetime
from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass


class History(Base):
    __tablename__ = "history"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    amount: Mapped[int] = mapped_column(Integer(), nullable=False)
    purchase_time: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer(), ForeignKey("product.id"))
    image_id: Mapped[int] = mapped_column(Integer(), ForeignKey("image.id"))
    post_id: Mapped[int] = mapped_column(Integer(), ForeignKey("post.id"))
