from fastapi import FastAPI
# Import routers from modules
from modules import api, ki_model, db, error_handling, sync, admin, console_manager

app = FastAPI(title="DevClip Server", description="Modular FastAPI Backend for DevClip")

# Include the routers in the FastAPI app
app.include_router(api.router)
app.include_router(ki_model.router)
app.include_router(db.router)
app.include_router(error_handling.router)
app.include_router(sync.router)
app.include_router(admin.router)

# Store the status of modules
modules_status = {
    "main": True,
    "api": False,
    "ki_model": False,
    "db": False,
    "error_handling": False,
    "sync": False,
    "admin": False
}

# Start a module (only if `main` is active)
def start_module(module_name):
    if not modules_status["main"]:
        return {"error": "Main module must be running."}
    modules_status[module_name] = True
    return {"message": f"{module_name} started."}

@app.get("/status")
def get_status():
    """Returns the status of all modules."""
    return modules_status

@app.post("/start/{module_name}")
def start_specific_module(module_name: str):
    """Starts a specific module if `main` is running."""
    if module_name in modules_status:
        return start_module(module_name)
    return {"error": "Invalid module name."}

# Include module routers
app.include_router(api.router)
app.include_router(ki_model.router)
app.include_router(db.router)
app.include_router(error_handling.router)
app.include_router(sync.router)
app.include_router(admin.router)

# Start console management in a separate thread
console_thread = threading.Thread(target=console_manager.run_console, daemon=True)
console_thread.start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
