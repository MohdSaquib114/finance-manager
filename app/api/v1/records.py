from fastapi import APIRouter

router = APIRouter(prefix="/records", tags=["records"])

@router.get("/")
async def get_records():
    return {"message": "Get all records"}