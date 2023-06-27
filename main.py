from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Jonathan"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#query parameter
@app.get("/raspberry")
async def read_item(time:datetime = datetime.now(),light: float = 0.0, temperature: float = 0.0):
    return {
        "TIME":time.strftime("%Y%m%d %H:%M:%S"),
        "LIGHT":light,
        "TEMPERATURE":temperature
    }