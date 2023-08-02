from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    from .currency import Currency

class Deal(Base):
    __tablename__ = 'deal'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    item: Mapped[str] = mapped_column(String(100))
    price: Mapped[int]

    currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    currency: Mapped["Currency"] = relationship("Currency")

    league: Mapped[str] = mapped_column(String(24))
    section: Mapped[str] = mapped_column(String(12))
    left: Mapped[int | None]
    top: Mapped[int | None]
    time: Mapped[datetime] = mapped_column()
    status: Mapped[str] = mapped_column(String(32))


