from fastapi import FastAPI, status

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search/featured", status_code=status.HTTP_200_OK)
async def featured():
    return {"featured": []}


@app.get("/search/promoted", status_code=status.HTTP_200_OK)
async def promoted():
    return {"promoted": []}


@app.get("/search", status_code=status.HTTP_200_OK)
async def search(query: str = "", skip: int = 0, limit: int = 10):
    return {"search": []}


@app.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(
    title: str,
    category: str,
    price: int,
    location: str,
    description: str,
    isNegotiable: bool,
):
    return {"id": 1}


@app.get("/product/{id}", status_code=status.HTTP_200_OK)
async def get_product(id):
    return {"data": ""}


@app.patch("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit_product(
    title: str,
    category: str,
    price: int,
    location: str,
    description: str,
    isNegotiable: bool,
):
    return {"status": 204}


@app.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id):
    return {"status": 204}
