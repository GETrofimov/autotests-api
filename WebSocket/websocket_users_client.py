import asyncio

import websockets

async def client():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        greeting = "Привет, сервер!"
        await websocket.send(greeting)
        for _ in range(5):
            message = await websocket.recv()
            print(message)

asyncio.run(client())
