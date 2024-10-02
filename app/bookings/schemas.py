from datetime import date

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    user_id: int
    room_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    
    class Config():
        # orm_mode=True
        from_attributes=True

#     Если мы попросим FastAPI вернуть объект, который нам дала Алхимия, мы получим
# ошибку. FastAPI не сможет автоматически конвертировать модель Алхимии в JSON
# (FastAPI автоматически конвертирует любой ответ пользователю в JSON). Для
# сериализации модели SQLAlchemy в модель Pydantic и затем в JSON нам необходимо
# создать Pydantic схему, которая будет в точности отражать ответ от Алхимии. Важно
# отметить, что для работы с ответом Алхимии нам необходимо обращаться к атрибутам
# через точку: Hotels.name или Hotels.location, а не Hotels["name"] и Hotels["location"].
# Для того, чтобы Pydantic мог обращаться к атрибутам модели Алхимии через точку (по
# умолчанию Pydantic обращается только через Hotels["..."] , мы обязаны указать
# внутри Pydantic схемы параметр orm_mode со значением True следующим образом:

    