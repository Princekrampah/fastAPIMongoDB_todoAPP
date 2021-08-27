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
def todo(todo) -> dict:
    return {
        "id": str(todo.get("_id", None)),
        "name": str(todo.get("name", None)),
        "description": str(todo.get("description", None)),
        "completed": str(todo.get("completed", None)),
        "date": str(todo.get("date", None)),
    }

def todos(todos) -> list:
    return [todo(todo) for todo in todos]
```


## Build The CRUD API