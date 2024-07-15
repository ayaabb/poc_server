from fastapi import APIRouter

router = APIRouter()

@router.get("/start")
def hello_text():
    return {"Message": "Hello ,I am your bot!"}

@router.get("/test")
def info():
    return {"Message": "It's a bot test!"}
