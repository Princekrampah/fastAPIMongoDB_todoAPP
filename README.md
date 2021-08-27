# FastAPI MongoDB Todo List

## Prerequisites

1. FastAPI basics
2. Python installed 
3. Mongodb Community server installed


## Install Dependencies

1. fastAPI
2. uvicorn
3. pymongo

```shell
$ pip install fastapi uvicorn pymongo pymongo[srv]
```

## Create the Project structure


## Edit main.py

```python
from fastapi import FastAPI

app = FastAPI()
```

run the server

## Edit database.py

create a file called database.py and add the following content inside of it

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/mydb")

db = client.todo_app

collection_name = db["todos_app"]
```

**Note: the `"mongodb://localhost:27017/mydb**"` is optional since be default MongoClient will connect to this port and route.**

If you want to use Atlas or an online mongoDB platform, the the URL to the cluster in place to the argument used in the instantiation on the MongoDB client


## Create the todos_*

Create the todos_* files in models, routes and schemas folders respectively

## Edit todos_model.py

```python
from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    description: str
    completed: bool
    date: str
```

## Edit todos_schemas.py

```python
def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"],
        "date": todo["date"],
    }

def todos_serializer(todos) -> list:
    return [todo_serializer(todo) for todo in todos]
```


## Build The CRUD API

```python
from fastapi import APIRouter

from models.todos_model import Todo
from config.database import collection_name

from schemas.todos_schema import todos_serializer, todo_serializer
from bson import ObjectId

todo_api_router = APIRouter()

# retrieve
@todo_api_router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return todos

@todo_api_router.get("/{id}")
async def get_todo(id: str):
    return todos_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@todo_api_router.post("/")
async def create_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    return todos_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@todo_api_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    return todos_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@todo_api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
```


## For The Video Tutorial And More Tutorials Visit [My YouTube Channel](https://www.youtube.com/channel/UCQf9BYcqr8pzKrY14ZyMsbg)