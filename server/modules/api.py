from fastapi import APIRouter, HTTPException
import logging

# Create a logger for the API module
logger = logging.getLogger(__name__)

router = APIRouter()

# Dummy data for API example
data_stream = []

@router.get("/api-example")
def api_example():
    """Example API endpoint."""
    return {"message": "This is an example of API module endpoint"}

@router.post("/data")
def add_data(data: dict):
    """Adds data to the data stream."""
    data_stream.append(data)
    logger.debug(f"Data added: {data}")
    return {"message": "Data added successfully"}

@router.get("/data")
def get_data():
    """Fetches all data from the stream."""
    return {"data": data_stream}

@router.delete("/data/{data_id}")
def delete_data(data_id: int):
    """Deletes data from the stream by index."""
    if 0 <= data_id < len(data_stream):
        deleted = data_stream.pop(data_id)
        logger.debug(f"Data deleted: {deleted}")
        return {"message": f"Data at index {data_id} deleted"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")

# New endpoint for showing module status
@router.get("/status")
def get_status():
    """Returns the status of the server and modules."""
    # Assuming the server is running
    return {"status": "Server is running", "modules": ["API", "KI Model", "DB", "Error Handling", "Sync", "Admin"]}
