from fastapi import APIRouter

router = APIRouter(prefix="/records", tags=["records"])

@router.get("/")
async def get_users():
    return {"message": "Get all users"}