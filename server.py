import asyncio
import json

from sanic import Sanic, response
from websockets.exceptions import ConnectionClosed

import AI

app = Sanic("software-lab2-git")


@app.route("/")
async def test(request):
    return await response.file('./static/index.html')


@app.websocket('/chat')
async def feed(request, ws):
    while True:
        try:
            message = await ws.recv()
            response = AI.get_response(message)
            for message in response:
                await ws.send(json.dumps({'data': message}))
                await asyncio.sleep(1.0)
        except ConnectionClosed:
            break


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
