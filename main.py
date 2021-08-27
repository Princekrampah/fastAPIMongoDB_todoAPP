from fastapi import FastAPI
from routes.todos_route import todo_api_router

app = FastAPI()

app.include_router(todo_api_router)

