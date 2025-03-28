from fastapi import APIRouter
import logging

# Create a logger for the Database module
logger = logging.getLogger(__name__)

router = APIRouter()

# Simulated database
db = []

@router.post("/add-entry")
def add_entry(entry: dict):
    """Adds an entry to the simulated database."""
    db.append(entry)
    logger.debug(f"Entry added: {entry}")
    return {"message": "Entry added successfully"}

@router.get("/get-entries")
def get_entries():
    """Fetches all entries from the simulated database."""
    return {"data": db}

@router.delete("/delete-entry/{entry_id}")
def delete_entry(entry_id: int):
    """Deletes an entry from the simulated database."""
    if 0 <= entry_id < len(db):
        deleted_entry = db.pop(entry_id)
        logger.debug(f"Entry deleted: {deleted_entry}")
        return {"message": f"Entry {entry_id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")
