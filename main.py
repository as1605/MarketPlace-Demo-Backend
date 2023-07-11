from fastapi import FastAPI, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from bson import ObjectId
import dotenv

dotenv.load_dotenv()

from database import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search/featured")
async def featured() -> list[Product]:
    result = await Products.find({"isFeatured": True}).to_list(10)
    return JSONResponse(status_code=status.HTTP_200_OK, content=parse_json(result))


@app.get("/search/promoted")
async def promoted() -> list[Product]:
    result = await Products.find({"isPromoted": True}).to_list(10)
    return JSONResponse(status_code=status.HTTP_200_OK, content=parse_json(result))


@app.get("/search")
async def search(query: str = "", skip: int = 0, limit: int = 10) -> list[Product]:
    result = await Products.find({"title": {"$regex": query}}).to_list(limit)
    return JSONResponse(status_code=status.HTTP_200_OK, content=parse_json(result))


@app.post("/product")
async def create_product(product: Product) -> Product:
    product_json = jsonable_encoder(product)
    new_product = await Products.insert_one(product_json)
    created_product = await Products.find_one({"_id": new_product.inserted_id})
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=parse_json(created_product)
    )


@app.get("/product/{id}", status_code=status.HTTP_200_OK)
async def get_product(id) -> Product:
    result = await Products.find_one({"_id": ObjectId(id)})
    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content=parse_json(result))
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.patch("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit_product(id, product: Product):
    await Products.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": jsonable_encoder(product)}
    )


@app.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id):
    await Products.delete_one({"_id": ObjectId(id)})
