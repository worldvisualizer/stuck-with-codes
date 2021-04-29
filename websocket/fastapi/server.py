from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

app = FastAPI()
app.debug = True

class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []


    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)


    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)


    async def send_message(
        self, status: str, message_type: str,
        message: dict, websocket: WebSocket
    ):
        await websocket.send_json(
            {
                "type": message_type,
                "status": status,
                "data": message
            }
        )

    async def broadcast(self, status, message_type, message):
        for conn in self.connections:
            await conn.send_message(status, message_type, message)


@app.get("/")
def home():
    """
    Serve static index page.
    """
    return FileResponse("public/index.html")


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message("200", "RESPONSE", {"message": data}, websocket)
            await manager.broadcast("200", "BROADCAST", {"message": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("200", "DISCONNECT_BROADCAST", {"message": "client left"})

