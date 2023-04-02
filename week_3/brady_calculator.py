"""
    Title: brady_calculator.py
    Author: Erin Brady
    Date: 2 April 2023
    Description: Simple calculator app to demonstrate use of Python Variables and Functions.
"""

# Calculation Functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

# Test calculation functions.
test_add = add(4, 4)
test_subtract = subtract(10, 6)
test_divide = divide(8, 2)
test_multiply = multiply(10, 2)

# Output tests to console.
print("4 + 4 is %s." % (test_add))
print("10 - 6 is %s" % (test_subtract))
print("8 / 2 is %s" % (test_divide))
print("10 * 2 is %s" % (test_multiply))
