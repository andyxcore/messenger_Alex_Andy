from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")


#DB

db = conn.db
collection = db.messages

messText = input()

emp_rec1 = {
        "name": "Alex",
        "text": MessText,
        "time": sysdate
        }
# Insert Data
InsCollection = collection.insert_one()