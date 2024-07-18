from dotenv import load_dotenv
import os
import random
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from pymongo.errors import PyMongoError

router = APIRouter()

load_dotenv('mongo_uri.env')
MONGODB_URI = os.getenv("MONGODB_URI")


def connect_to_mongo(MONGODB_URI, db_name, coll_name):
    try:
        client = MongoClient(MONGODB_URI)
        db = client[db_name]
        collection = db[coll_name]
        return collection

    except ValueError as e:
        print(f"Value Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    except PyMongoError as e:
        print(f"PyMongo Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to connect to MongoDB.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.get("/generate")
def generate():
    try:
        random_num = random.randint(1, 1000)
        collection = connect_to_mongo(MONGODB_URI,"generate_db","random_numbers")
        collection.insert_one({"number": random_num})
        return {"number": random_num}

    except HTTPException as he:
        raise he
    except PyMongoError as pme:
        print(f"PyMongo Error: {pme}")
        raise HTTPException(status_code=500, detail="Failed to insert the random number into MongoDB.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred while generating the number.")
