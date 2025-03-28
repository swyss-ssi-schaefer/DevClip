from fastapi import APIRouter, HTTPException
import logging

# Create a logger for the Error Handling module
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/error-test")
async def test_error():
    """Simulates an error."""
    raise HTTPException(status_code=500, detail="An internal error occurred")

@router.get("/error-status")
def error_status():
    """Returns a simple error message."""
    return {"status": "Error handling is working"}
