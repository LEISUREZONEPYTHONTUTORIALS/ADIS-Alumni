import websockets

import asyncio

PORT = 8000

connected = set()

async def echo(websocket,path):

  connected.add(websocket)

  try:

    async for message in websocket:

      print("Client:",message)

      for conn in connected:

        if conn!=websocket:

          await conn.send("Unknown:",message)

  except websockets.exceptions.ConnectionClosed as e:

    print(e)

start = websockets.serve(echo,"0.0.0.0",PORT)

asyncio.get_event_loop().run_until_complete(start)

asyncio.get_event_loop().run_forever()
