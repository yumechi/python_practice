from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        default=None,
        min_length=3,
        max_length=50,
        # 正規表現も使える
        # regex="^fixedquery$"
    ),
):
    """
    Queryを使ったバリデーションの例。下記をはチェック。

    * 長さが3以上
    * 長さが50以下

    サンプルのregexを設定すると受け取りパターンが固定になる（文字列開始と終了が指定されているため）
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_2/")
async def read_items_2(q: str = Query("fixedquery", min_length=3)):
    """
    初期値と min_length の組み合わせ
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_3/")
async def read_items_3(q: str = Query(..., min_length=3)):
    """
    必須パラメーターを使う。
    必須とする場合は ... にする。
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_4/")
async def read_items_4(q: list[str] = Query(["foo", "bar"])):
    """
    list を使うケース。
    初期値を使わない場合は `q: list = Query[]` と書ける。
    """

    query_item = {"q": q}
    return query_item


@app.get("/items_5/")
async def read_items_5(
    q: Optional[str] = Query(
        None,
        title="クエリ文字列",
        description="これはクエリの文字列ですという説明",
        min_length=3,
    )
):
    """
    titleやdescriptionを使うと OpenAPI 側で見たときに説明が追加される。
    """

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_6/")
async def read_items_6(
    q: Optional[str] = Query(None, alias="item-query", deprecated=True)
):
    """
    aliasを使うとパラメータとして受け取るkey名を変更できる。
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
