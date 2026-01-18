# lists.py
# This file contains basic examples of working with Python lists.
# Topic: creating lists, accessing items, updating, adding, removing, and looping.

# Creating a list and accessing items
fruits = ["apple", "banana", "cherry","plum", "orange", "strawberry"]
print(fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
# --------------------------------------------

# Changing list items
numbers = [10, 20, 30, 40]
numbers[1] = 25
print("Updated list: ", numbers)

# ------------------------------------------------------------
# Adding items to a list
students = ["Ali", "Vali"]
students.append("Hasan")
print("Students list:", students)

# ------------------------------------------------------------
# Removing items from a list
colors = ["red", "green", "blue", "yellow"]
colors.remove("blue")

print("Colors after removal:", colors)

# ------------------------------------------------------------
# Looping through a list
prices = [12000, 15000, 18000]
total = 0

for price in prices:
    total += price

print("Total price:", total)
