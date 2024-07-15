from fastapi import FastAPI

server = FastAPI()

@server.get("/start")
def hello_text():
    return {"Message": "Hello ,I am your bot!"}

@server.get("/test")
def info():
    return {"Message": "It's a bot test!"}
