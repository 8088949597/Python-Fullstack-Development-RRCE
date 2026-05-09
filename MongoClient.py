from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://Kavya:Kavya8088@cluster0.ltp9tww.mongodb.net/?retryWrites=true&w=majority")

# Create / Access database
db = client["libraryDB"]

# Create / Access collection
books_collection = db["books"]

# -------------------------------
# 1. CREATE OPERATION (INSERT)
# -------------------------------
books_data = [
    {
        "book_id": 101,
        "title": "Data Structures",
        "author": "Mark Allen",
        "genre": "Computer Science",
        "status": "Available"
    },
    {
        "book_id": 102,
        "title": "Database Systems",
        "author": "Henry Roberts",
        "genre": "Computer Science",
        "status": "Available"
    },
    {
        "book_id": 103,
        "title": "English Literature",
        "author": "John Smith",
        "genre": "Literature",
        "status": "Available"
    }
]

# Insert only if collection is empty
if books_collection.count_documents({}) == 0:
    books_collection.insert_many(books_data)
    print("3 book records inserted successfully.")
else:
    print("Books already exist in the collection.")

# -------------------------------
# 2. READ OPERATION (RETRIEVE)
# -------------------------------
print("\nAll Books in Collection:")
for book in books_collection.find():
    print(book)

print("\nBooks in Genre = 'Computer Science':")
for book in books_collection.find({"genre": "Computer Science"}):
    print(book)

# -------------------------------
# 3. UPDATE OPERATION
# -------------------------------
result = books_collection.update_one(
    {"book_id": 101},
    {"$set": {"status": "Issued"}}
)

if result.modified_count > 0:
    print("\nBook with book_id 101 updated successfully.")
else:
    print("\nNo book updated.")

print("\nUpdated Book Record:")
print(books_collection.find_one({"book_id": 101}))

# -------------------------------
# 4. DELETE OPERATION
# -------------------------------
result = books_collection.delete_one({"book_id": 103})

if result.deleted_count > 0:
    print("\nBook with book_id 103 deleted successfully.")
else:
    print("\nNo book deleted.")

print("\nFinal Books in Collection:")
for book in books_collection.find():
    print(book)