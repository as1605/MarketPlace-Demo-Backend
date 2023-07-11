from pydantic import BaseModel
import motor.motor_asyncio
import os
import json
from bson import json_util
from bson import ObjectId
from typing import Union


class Product(BaseModel):
    _id: Union[ObjectId, None]
    title: str
    category: str
    price: int
    location: str
    description: str
    img_url: Union[str, None]  # Optional field for including image URL
    metadata_user: Union[
        str, None
    ]  # Optional field for storing info about buyer or seller
    isNegotiable: bool
    isFeatured: bool
    isPromoted: bool


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.marketplace
Products = db["products"]


def parse_json(data):
    return json.loads(json_util.dumps(data))
