/**
	Title: brady-assignment5.2.js
    Author: Erin Brady
    Date: 15 April 2023
    Description: MongoDB Queries for the users collection.
*/

// Add a new user to the users collection.
db.users.insertOne({
    firstName: 'Igor',
    lastName: 'Stravinsky',
    employeeId: '1013',
    email: 'istravinsky@me.com',
    dateCreated: new Date(Date.now())
})

// Update Mozart's email address to mozart@me.com.
db.users.updateOne({
    lastName: 'Mozart'
}, { $set: {
    email: 'mozart@me.com'
}})

// Prove the email address was updated.
db.users.findOne({email: 'mozart@me.com'})

// List all documents in the users collection.
db.users.find().toArray()
