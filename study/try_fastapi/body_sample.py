from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict |= {"price_with_tax": price_with_tax}
    return item_dict


# 判断ルール的には下記
# パラメーターがパスでも宣言されている場合は、パスパラメータとして判断
# パラメーターが単数型(int, float, str, bool)の場合は、クエリパラメータとして判断
# パラメータが Pydantic モデルの型である場合、リクエストボディ
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result |= {"q": q}
    return result
