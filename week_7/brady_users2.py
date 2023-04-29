"""
  Title: brady-users2.py
  Author: Erin Brady
  Date: 29 April 2023
  Description: Exercise 7.3: Python with MongoDB, Part 2
"""

from pymongo import MongoClient
import datetime

# Build a connection string to connect to web335DB.
print("Connect to MongoDB.\n")

client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.nhzwaya.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access web335DB.
db = client['web335DB']

# Create a new user document.
print("Create a new user document.")

new_user = {
    
    "firstName": "Antonio",
    "lastName": "Vivaldi",
    "employeeId": "1014",
    "email": "avivaldi@me.com",
    "dateCreated": datetime.datetime.now()
}

new_user_result = db.users.insert_one(new_user)

# Display the newly created document.

created_user = db.users.find_one({"employeeId": "1014"}, {"firstName": 1, "lastName": 1, "employeeId": 1})

print("Created new user: ")
print(created_user)

# Update the email of address of the document I created.
print("\nUpdate the email of address of the document I created.")

db.users.update_one({"email": "avivaldi@me.com"}, {"$set": {"email": "vivaldi@example.com"}})

# Display the updated document.
updated_user = db.users.find_one({"email": "vivaldi@example.com"}, {"firstName": 1, "lastName": 1, "email": 1})

print("Updated user: ")
print(updated_user)

# Delete the document I created.
print("\nDelete the document I created.")

db.users.delete_one({"employeeId": "1014"})

# Prove the document was deleted.
deleted_user = db.users.find_one({"employeeId": "1014"}, {"firstName": 1, "lastName": 1, "employeeId": 1})

print("Attempt to find deleted document: ")
print(deleted_user)
