from fastapi import FastAPI;
import json
app = FastAPI()


def load_data():
    with open('dumy.data.json') as f:
        data = json.load(f)
    return data


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get('/about')
def about():
    return {"message": "About the Page information"}


@app.post("/items/")
def create_item():
    return {"message": "Item created successfully"}


@app.get("/data/")
def get_data():
    data = load_data()
    return {"data": data}