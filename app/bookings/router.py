from datetime import date
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends

# from app.database import async_session_maker
# from app.bookings.models import Bookings
# from sqlalchemy import select
from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users
# from fastapi_versioning import version

router=APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get('')
# @version(1)
async def get_bookings(user: Users=Depends(get_current_user)) -> List[SBooking]:
    print(user, type(user), user.email)
    result= await BookingDAO.find_all(user_id=user.id)
    return result

@router.post('') 
# @version(2)
async def add_booking(
    background_tasks: BackgroundTasks,
    room_id: int, 
    date_from: date, 
    date_to: date ,
    user: Users=Depends(get_current_user)
    ):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to )
    if not booking:
        raise RoomCannotBeBookedException
    
    # booking_dict = parse_obj_as(SBooking, booking).dict() - этот способ устарел

    # Используем метод валидации напрямую из Pydantic
    # Используем метод валидации и новый метод model_dump вместо dict
    # Преобразуем booking в сериализуемый формат перед передачей в Celery
    booking_dict = SBooking.model_validate(booking).model_dump()
    
    # Передаем сериализуемый словарь в Celery
    # send 
    #вариант с Background Tasks 
    background_tasks.add_task(send_booking_confirmation_email, booking_dict, user.email)
    return  booking

        
    

# @router.get('')
# async def get_bookings():
#     async with async_session_maker() as session:
#         query=select(Bookings)
#         result= await session.execute(query)
#         return result.mapping().all()
   
# @router.get("/{booking_id}")
# def get_bookings2(booking_id):
#     pass




