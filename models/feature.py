from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from .base import Base

# class Base(DeclarativeBase):
#     pass


class Feature(Base):
    __tablename__ = "feature"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    value: Mapped[str] = mapped_column(String(), nullable=False)
