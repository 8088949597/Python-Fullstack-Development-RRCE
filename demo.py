from pymongo import MongoClient

client = MongoClient("mongodb+srv://Kavya:Kavya8088@cluster0.ltp9tww.mongodb.net/?retryWrites=true&w=majority")

db = client["mydb"]
collection = db["students"]

data = {
    "name": "Sumanth",
    "age": 26,
    "branch": "civil"
}

collection.insert_one(data)

print("Data inserted successfully")

 
