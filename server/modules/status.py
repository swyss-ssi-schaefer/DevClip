from fastapi import APIRouter
import redis
import json

# Redis-Client initialisieren
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

router = APIRouter()

# Status-Modell zur Verwaltung von Statusdaten
class Status:
    def __init__(self):
        self.modules_status = {
            "api": False,
            "ki_model": False,
            "db": False,
            "error_handling": False,
            "sync": False,
            "admin": False
        }
        self.connected_clients = []
        self.sync_status = "Idle"  # Beispiel: "Idle", "In Progress", "Completed"
    
    def save_status(self):
        """Speichert den aktuellen Status in Redis."""
        redis_client.set("modules_status", json.dumps(self.modules_status))
        redis_client.set("connected_clients", json.dumps(self.connected_clients))
        redis_client.set("sync_status", self.sync_status)
    
    def load_status(self):
        """Lädt den Status aus Redis."""
        self.modules_status = json.loads(redis_client.get("modules_status") or "{}")
        self.connected_clients = json.loads(redis_client.get("connected_clients") or "[]")
        self.sync_status = redis_client.get("sync_status") or "Idle"
    
    def get_status(self):
        """Gibt den aktuellen Status der Module, Clients und Sync zurück."""
        return {
            "modules_status": self.modules_status,
            "connected_clients": self.connected_clients,
            "sync_status": self.sync_status
        }

status_manager = Status()

@router.get("/status")
def get_system_status():
    """Gibt den aktuellen Status der Module und Clients zurück."""
    status_manager.load_status()
    return status_manager.get_status()

@router.post("/update_status")
def update_status(module_name: str, status: bool):
    """Aktualisiert den Status eines Moduls."""
    if module_name in status_manager.modules_status:
        status_manager.modules_status[module_name] = status
        status_manager.save_status()
        return {"message": f"{module_name} status updated to {status}"}
    else:
        return {"error": "Invalid module name"}

@router.post("/add_client")
def add_client(client_name: str):
    """Fügt einen verbundenen Client hinzu."""
    status_manager.connected_clients.append(client_name)
    status_manager.save_status()
    return {"message": f"Client {client_name} added"}

@router.post("/remove_client")
def remove_client(client_name: str):
    """Entfernt einen verbundenen Client."""
    if client_name in status_manager.connected_clients:
        status_manager.connected_clients.remove(client_name)
        status_manager.save_status()
        return {"message": f"Client {client_name} removed"}
    else:
        return {"error": "Client not found"}

@router.post("/sync_start")
def start_sync():
    """Startet die Synchronisation und aktualisiert den Status."""
    status_manager.sync_status = "In Progress"
    status_manager.save_status()
    return {"message": "Sync started"}

@router.post("/sync_complete")
def complete_sync():
    """Beendet die Synchronisation und aktualisiert den Status."""
    status_manager.sync_status = "Completed"
    status_manager.save_status()
    return {"message": "Sync completed"}
