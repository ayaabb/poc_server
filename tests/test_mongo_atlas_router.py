import os
import pytest
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi.testclient import TestClient
from app.server import server
from routes.mongo_atlas_router import connect_to_mongo

load_dotenv('mongo_uri.env')
MONGODB_URI = os.getenv("MONGODB_URI")

client = TestClient(server)


def test_generate_number():
    response = client.get("/generate")
    if response.status_code == 200:
        data = response.json()
        assert "number" in data
        assert 1 <= data["number"] <= 1000
        coll = connect_to_mongo(MONGODB_URI, "generate_db", "random_numbers")
        result = coll.find_one({"number": data["number"]})
        assert result is not None

    elif response.status_code == 500:
      assert ("Failed to insert the random number" or "An unexpected error occurred while generating the number."
              in response.json()["detail"])

