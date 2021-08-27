from pymongo import MongoClient



client = MongoClient("mongodb+srv://prince:<password>@cluster0.xfinu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.todo_app

collection_name = db["todos_app"]
