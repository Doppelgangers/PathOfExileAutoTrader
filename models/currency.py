from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Currency(Base):
    __tablename__ = 'currency'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_ru: Mapped[str] = mapped_column(String(50))
    name_en: Mapped[str] = mapped_column(String(50))
    chaos_price: Mapped[int]

    def __str__(self):
        return f"Currency [id: {self.id}, name_en: {self.name_en}, name_ru: {self.name_ru}, chaos_price: {self.chaos_price} "

    def __repr__(self):
        return str(self)

