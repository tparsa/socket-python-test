import asyncio
import websockets


async def hello(websocket, path):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosed:
            break
        print(f"Client said: {message}")

        response = f"The mighty server telling ya {message}"
        try:
            await websocket.send(response)
        except webscokets.ConnectionClosed:
            break
        print(f"Server said: {response}")


start_server = websockets.serve(hello, "localhost", 8765)

loop = asyncio.get_event_loop()

loop.run_until_complete(start_server)
loop.run_forever()
