from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code=500
    detail=''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class RoomCannotBeBookedException ( BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="Нет свободных комнат для бронирования"


class UserAlreadyExistsException ( BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"


class IncorrectEmailOrPassword ( BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный email или пароль"


class TokenExpiredException ( BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен истек"

class TokenAbsentException  ( BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"

class IncorrectTokenFormatException  (BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"


class UserException (BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED



class CannotBookHotelForLongPeriod(BookingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Невозможно забронировать отель сроком более месяца"

class DateFromCannotBeAfterDateTo(BookingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Дата заезда не может быть позже даты выезда"