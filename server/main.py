import threading
from server.modules import admin, api, console_manager, db, error_handling, ki_model, status, sync
import uvicorn
from fastapi import FastAPI
import logging

# Initialize logging for debug mode
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



app = FastAPI(title="DevClip Server", description="Modular FastAPI Backend for DevClip")

# Include the routers in the FastAPI app
app.include_router(api.router)
app.include_router(ki_model.router)
app.include_router(db.router)
app.include_router(error_handling.router)
app.include_router(sync.router)
app.include_router(admin.router)
app.include_router(status.router)

# Start console management in a separate thread
if hasattr(console_manager, "run_console"):
    console_thread = threading.Thread(target=console_manager.run_console, daemon=True)
    console_thread.start()

# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
