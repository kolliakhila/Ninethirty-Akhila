from fastapi import FastAPI

app=FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id:int):
    return {"user_id":user_id,"user_name":"Akhila"}

@app.get("/product_id:{product_id}")
def read_product(product_id:str):
    return {"product_id": product_id}

@app.get("/users")
def read_all_users():
    users=[
        {"user_id":1,"name":"Bannu"},
        {"user_id":2,"name":"Sunny"},
        {"user_id":3,"name":"Bhavi"},
    ]
    return {"users":users}