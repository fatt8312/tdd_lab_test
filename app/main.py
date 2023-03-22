from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"callname": "World1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello/{name}")
def read_name(name: str = None):
    return {"callname": name}

@app.post("/callname/{name}")
def call_name(name: str):
    return {"callname": name}

handler = Mangum(app)
