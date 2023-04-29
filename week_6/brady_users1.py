"""
  Title: brady-users1.py
  Author: Erin Brady
  Date: 20 April 2023
  Description: Exercise 6.3: Python with MongoDB
"""

from pymongo import MongoClient

# Build a connection string to connect to web335DB.
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.nhzwaya.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access web335DB.
db = client['web335DB']

# Display all documents in the user’s collection.
print("Display all documents in the user’s collection.")
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

# Display a document where the employeeId is 1011
print("Display a document where the employeeId is 1011.")
print(db.users.find_one({"employeeId": "1011"}, {"firstName": 1, "lastName": 1, "employeeId": 1}))

# Display a document where the lastName is Mozart
print("Display a document where the lastName is Mozart.")
print(db.users.find_one({"lastName": "Mozart"}, {"firstName": 1, "lastName": 1, "employeeId": 1}))
