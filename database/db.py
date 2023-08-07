from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import Session, selectinload

import settings
from models import Base, Currency, Deal


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):

    def __init__(self, path_sqlalchemy: str = ''):
        if not path_sqlalchemy:
            path_sqlalchemy = settings.SQLALCHEMY_PATH
        self.engine = sqlalchemy.create_engine(path_sqlalchemy, echo=settings.SQLALCHEMY_ECHO)
        Base.metadata.create_all(bind=self.engine)

        self.session = Session(self.engine)

    def __del__(self):
        self.session.close()


class Database_Task(Database):

    def __init__(self, path_sqlalchemy: str = ''):
        super().__init__(path_sqlalchemy=path_sqlalchemy)

    def fetch_currency_for_name(self, name: str) -> Currency | None:
        stmt = sqlalchemy.select(Currency).where(Currency.name_ru == name or Currency.name_en == name)
        cur: Currency | None = self.session.scalar(stmt)
        return cur

    def create_deal(self, name, item, price, currency, league, section, left, top, status="pending"):
        currency = self.fetch_currency_for_name(name=currency)
        deal = Deal(
            name=name,
            item=item,
            price=price,
            currency=currency,
            league=league,
            section=section,
            left=left,
            top=top,
            time=datetime.now(),
            status=status
        )
        self.session.add(deal)
        self.session.commit()

    def fetch_task(self) -> Deal | None:
        stmt = sqlalchemy.select(Deal).where(Deal.status == "pending").options(selectinload(Deal.currency))
        deal: Deal | None = self.session.scalar(stmt)
        return deal
