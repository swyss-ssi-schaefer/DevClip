from fastapi import APIRouter
import logging

# Create a logger for the Admin module
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/admin-status")
def get_admin_status():
    """Returns admin status."""
    return {"status": "Admin module is running"}
