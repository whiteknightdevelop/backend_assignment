from typing import Optional
from fastapi import Request, FastAPI
from currency import *
import uvicorn

app = FastAPI()

PORT = 8000
HOST = "0.0.0.0"

currency_list = CurrencyList()

@app.get("/")
def read_root():
    return currency_list.currencies

@app.post("/update-data/")
async def update_data(request: Request):
    js = await request.json()
    print(js)
    currency_list.currencies = js


if __name__ == '__main__':
    uvicorn.run(app, port=PORT, host=HOST)