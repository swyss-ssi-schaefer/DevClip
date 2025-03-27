from fastapi import APIRouter

router = APIRouter()

@router.get("/sync-test")
async def test_sync():
    return {"message": "Sync module works"}
