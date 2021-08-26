import asyncio
import websockets
import sys

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        for line in sys.stdin:
            message = line

            await ws.send(message)
            print(f"Client said: {message}")

            response = await ws.recv()
            print(f"Server said {response}")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
