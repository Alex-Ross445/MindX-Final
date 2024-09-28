import asyncio
from websockets.server import serve

async def server(websocket, path):
    async for message in websocket:
        await websocket.send(f'Your message: {message}')

start_server = websockets.serve(server, "localhost", 9999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()