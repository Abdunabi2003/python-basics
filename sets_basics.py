
# -----------------------------------
# Sets Basics - Practice Problems
# Topic: creating sets, adding/removing elements,
# and removing duplicates
# -----------------------------------


# -----------------------------------
# Problem 1: Remove Duplicates
# Given a list of numbers, create a set
# and print the count of unique elements.
# -----------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)
print("Count:", len(unique_numbers))


# -----------------------------------
# Problem 2: Add Elements to a Set
# Ask the user to enter 5 numbers.
# Add them to a set and print:
# - the final set
# - the count of unique numbers
# -----------------------------------

numbers = set()

for _ in range(5):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Final set:", numbers)
print("Unique numbers count:", len(numbers))

# -----------------------------------
# Problem 3: Remove Elements from a Set
# Remove an existing element using remove()
# Try to remove a non-existing element using discard()
# -----------------------------------

colors = {"red", "green", "blue", "yellow"}

colors.remove("green")
colors.discard("black")   

print(colors)


# -----------------------------------
# Problem 4: Remove Duplicates from a List
# Convert a list with duplicate names
# into a set to keep only unique values.
# -----------------------------------

names = ["Ali", "Vali", "Ali", "Zara", "Vali", "Sami", "Zara"]

unique_names = set(names)
result = list(unique_names)

print(result)

# -----------------------------------
# Problem 5: Unique Items Count
# Convert a list with duplicates into a set
# and count how many unique elements exist.
# -----------------------------------

items = [10, 20, 10, 30, 40, 20, 50, 30]

unique_items = set()

for item in items:
    unique_items.add(item)

print(unique_items)
print("Unique count:", len(unique_items))

