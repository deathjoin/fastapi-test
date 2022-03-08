from fastapi import APIRouter


router = APIRouter()


@router.get("/login-test")
async def login_test():
    return {"message": "login test"}
