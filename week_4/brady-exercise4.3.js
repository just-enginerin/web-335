/**
	Title: brady-assignment4.3.js
    Author: Erin Brady
    Date: 9 April 2023
    Description: MongoDB Queries for the users collection.
*/

// Query to display all of the documents in the user’s collection.
db.users.find()

// Query find the user with an email address of jbach@me.com.
db.users.find({email: 'jbach@me.com'})

// Query to find a user with the last name of Mozart.
db.users.find({lastName: 'Mozart'})

// Query to find a user with a first name of Richard.
db.users.find({firstName: 'Richard'})

// Query to find a user with an employeeId of 1010.
db.users.find({employeeId: '1010'})
