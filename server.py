from fastapi import FastAPI
from routes import mongo_atlas_router,simple_commands_router
server = FastAPI()

server.include_router(simple_commands_router.router)
server.include_router(mongo_atlas_router.router)