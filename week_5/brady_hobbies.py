"""
	Title: brady-hobbies.js
  Author: Erin Brady
  Date: 16 April 2023
  Description: Python Conditionals, Lists, and Loops.
"""

hobbies = [
  'knitting',
  'hiking',
  'kayaking',
  'gardening',
  'chess'
]

# List all Hobbies in console
for hobby in hobbies:
  print(hobby)


days_of_week = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  "Thursday",
  "Friday",
  "Saturday"
]

# Display whether or not each day is a work day.
for day in days_of_week:
  if day == 'Saturday' or day == 'Sunday':
    print(day + ': You are off! Go enjoy your hobbies.')
  else:
    print(day + ': It is a work day.')
