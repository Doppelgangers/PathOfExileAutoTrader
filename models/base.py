from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

    def __str__(self):
        attributes = ""
        for attr, value in self.__dict__.items():
            if attr[0] != "_" and attr[0] != "__":
                attributes += f"{attr}: {value}, "
        atr = attributes[:-2]
        return f"{self.__class__.__name__} {'{'}{atr}{'}'} "

    def __repr__(self):
        return str(self)
