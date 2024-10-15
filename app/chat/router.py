from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.database import async_session_maker #get_async_session
from app.chat.models import Messages
from sqlalchemy import insert, select
#from sqlalchemy.ext.asyncio import AsyncSession

router=APIRouter(
    prefix='/chat',
    tags=["Chat"]
)
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
#подключение нового пользователя, добавление его в список
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
#удаление пользователя, удаление его  из списка
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
#отправка персонального сообщения только одному  клиенту
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
#отправка сообщений всем клиентам
    async def broadcast(self, message: str, add_to_db: bool=False):
        if add_to_db:
            await self.add_messages_to_database(message)
        for connection in self.active_connections:
            await connection.send_text(message)
#сохранение сообщений в БД
    @staticmethod
    async def add_messages_to_database(message:str):
         async with async_session_maker() as session:
             stmt=insert(Messages).values(message=message)
             await session.execute(stmt)
             await session.commit()

manager = ConnectionManager()

#показать последние 5 сообщений
@router.get('/last_messages')
# async def get_last_messages(
#     session: AsyncSession = Depends(get_async_session)
# ):
async def get_last_messages(): 
    async with async_session_maker() as session:
  # Сначала получаем последние 5 сообщений
        query = select(Messages).order_by(Messages.id.desc()).limit(5)
        result = await session.execute(query)
        
        # Извлекаем все сообщения из результата scalars() возвращает только объекты
        messages = result.scalars().all()
        
        # Переворачиваем список сообщений, чтобы они были в порядке возрастания
        messages.reverse()
        
        messages_list = [msg.as_dict() for msg in messages]  # Преобразуем сообщения в словари
        return messages_list



@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True: #ждем сообщения от клиента
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)