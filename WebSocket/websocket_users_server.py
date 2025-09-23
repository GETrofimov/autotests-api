import asyncio

import websockets
from websockets import ServerConnection

# Функция нужна для того, чтобы сервер возвращал n сообщений 
def prepare_response(message):
    for m in range(5):
        yield f"{m +1} Cообщение пользователя: {message}"
    
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for message in prepare_response(message):
            await websocket.send(message)
        

# Запускаем WebSocket-сервер. Порт 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())