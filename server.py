import asyncio
import websockets


async def hello(websocket, path):
    while True:
        try:
            name = await websocket.recv()
        except websockets.ConnectionClosed:
            break
        print(f"Client said: {name}")

        asghar = f"Hello {name}"
        try:
            await websocket.send(asghar)
        except webscokets.ConnectionClosed:
            break
        print(f"Server said: {asghar}")


start_server = websockets.serve(hello, "localhost", 8765)

loop = asyncio.get_event_loop()

loop.run_until_complete(start_server)
loop.run_forever()
