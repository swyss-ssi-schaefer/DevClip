from fastapi import APIRouter

router = APIRouter()

@router.get("/error-test")
async def test_error():
    return {"message": "Error handling works"}
