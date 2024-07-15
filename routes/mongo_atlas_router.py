
import os
import random

from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
router = APIRouter()

load_dotenv('mongo_uri.env')

MONGODB_URI = os.getenv("MONGODB_URI")
try:
    if MONGODB_URI:

        client = MongoClient(MONGODB_URI)
        print(MONGODB_URI)
        db = client["generate_db"]
        collection = db["random_numbers"]
    else:
        print("Warning: No MONGO_URI found. ")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@router.get("/generate")
def generate():
    random_num = random.randint(1, 1000)

    result = collection.insert_one({"number": random_num})

    if result.inserted_id:
        return {"number": random_num}
    else:
        raise HTTPException(status_code=500, detail="Failed to store the random number.")


