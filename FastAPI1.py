from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def retrieve():
    return "Introduction of FastAPI"

@app.get("/name")
def get():
    return "This is just intro for get method"