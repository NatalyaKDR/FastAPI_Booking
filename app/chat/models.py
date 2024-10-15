from sqlalchemy import Column, Integer, String
from app.database import Base

class Messages(Base):
    __tablename__= "messages"
    id=Column(Integer, primary_key=True)
    message=Column(String)

    # когда мы будем использовать данные из этой таблицы (отправлять их  в js)
    # нам нужно чтобы они были не в формате sqlalchemy, а в json формате
    # для этого добавим метод который позволит при обращении messages.as_dict получать данные
    # в формате словаря который можно конвертировать в json

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


