/**
	Title: brady-assignment6.2.js
    Author: Erin Brady
    Date: 22 April 2023
    Description: Assignment 6.2: Aggregate Queries
*/

// Show a list of documents in the houses collection.
db.houses.find()

// Show a list of documents in the students collection.
db.students.find()

// Query to add a document to the students collection.
console.log(db.students.insertOne({firstName: 'Harry', lastName:'Potter', studentId: 's1019', houseId: 'h1007'}))

// Query to delete the newly added document.
console.log(db.students.deleteOne({studentId: 's1019'}))

// Query to show a list of students by house.
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house"
      }
    }
])
  

// Query to show a list of students for house Gryffindor.
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house"
      }
    },
    {
      $match: {
        houseId: 'h1007'
      }
    }
])

// Query to show a list of students for the Eagle mascot.
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house"
      }
    },
    {
      $match: {
        'house.mascot': 'Eagle'
      }
    }
])
