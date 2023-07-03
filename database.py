from pydantic import BaseModel
import motor.motor_asyncio
import os
import json
from bson import json_util


class Product(BaseModel):
    title: str
    category: str
    price: int
    location: str
    description: str
    isNegotiable: bool
    isFeatured: bool
    isPromoted: bool


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.marketplace
Products = db["products"]


def parse_json(data):
    return json.loads(json_util.dumps(data))