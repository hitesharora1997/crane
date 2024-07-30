import asyncio
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.crane.crane import Crane
from backend.crane.state_manager import StateManager
from backend.crane.models import CraneState, Origin
from typing import Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allow CORS for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Serve static files from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

crane = Crane()
state_manager = StateManager(crane)

@app.get("/")
async def root():
    return FileResponse('static/index.html')

@app.post("/update_state")
async def update_state(state: CraneState):
    logger.info(f"Received update_state request: {state}")
    state_manager.update_state(state.model_dump())
    return {"message": "State updated"}

@app.post("/solve_ik")
async def solve_ik(target_position: Tuple[float, float, float]):
    logger.info(f"Received solve_ik request: {target_position}")
    state_manager.solve_ik(target_position)
    return {"message": "IK solved"}

@app.post("/update_origin")
async def update_origin(origin: Origin):
    logger.info(f"Received update_origin request: {origin}")
    state_manager.update_origin(origin)
    return {"message": "Origin updated"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            state = crane.to_dict()
            await websocket.send_json(state)
            await asyncio.sleep(0.1)
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        try:
            await websocket.close()
        except RuntimeError:
            pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)