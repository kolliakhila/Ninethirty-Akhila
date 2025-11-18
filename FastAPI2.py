from fastapi import FastAPI,HTTPException

app=FastAPI()

items={}

@app.get("/")
def get_items():
    return items

@app.post("/items")
def creation(item_id:int,item:dict):
    item_id=max(items.keys(),default=0)+1
    items[item_id]=item
    return {"created":{"item_id":item_id,"items":item}}

@app.put("/items")
def update_item(item_id:int,item:dict):
    if item_id not in items:
        items[item_id]=item
        return {"added":{"item_id":item_id,"item":item}}
    items[item_id]=item
    return{"updated":{"item_id":item_id,"item":item}}

@app.delete("/items")
def delete(item_id:int):
    if item_id in items:
        del items[item_id]
        return {"deleted":item_id}
    raise HTTPException(status_code=404,detail="item not found")
