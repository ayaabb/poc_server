from fastapi import FastAPI

server = FastAPI()

@server.get("/")
def hello_text():
    return {"Message":"Hello there!"}
