
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

# -----------------------------------
# Problem 1: Unique Visitors (Union)
# Combine visitors from two different days
# and keep only unique user names.
# -----------------------------------

day_one_visitors = {"Ali", "Vali", "Zara"}
day_two_visitors = {"Zara", "Sami", "Ali"}

all_unique_visitors = day_one_visitors.union(day_two_visitors)
# alternative way:
# all_unique_visitors = day_one_visitors | day_two_visitors

print(all_unique_visitors)


# -----------------------------------
# Problem 2: Common Customers (Intersection)
# Find users who visited both days.
# -----------------------------------

day_one_visitors = {"Ali", "Vali", "Zara"}
day_two_visitors = {"Zara", "Sami", "Ali"}

common_visitors = day_one_visitors.intersection(day_two_visitors)
# alternative way:
# common_visitors = day_one_visitors & day_two_visitors

print(common_visitors)

# -----------------------------------
# Problem 3: New Signups (Difference)
# Find users who signed up this period
# but were not present in the previous one.
# -----------------------------------

last_month_users = {"Ali", "Vali", "Zara"}
this_month_users = {"Ali", "Zara", "Sami", "Kamila"}

new_users = this_month_users.difference(last_month_users)
# alternative way:
# new_users = this_month_users - last_month_users

print(new_users)

# -----------------------------------
# Problem 4: Username Check (Membership)
# Check if a username already exists
# in the registered users set.
# -----------------------------------

registered_usernames = {"ali123", "zara_dev", "sami99"}

username_to_check = "ali123"

exists = username_to_check in registered_usernames
print(exists)

# -----------------------------------
# Problem 5: Warehouse Product Comparison
# Remove duplicates from product lists
# and find:
# - all unique products (union)
# - common products (intersection)
# -----------------------------------

warehouse_one = [101, 102, 103, 101, 104]
warehouse_two = [103, 105, 102, 102]

unique_warehouse_one = set(warehouse_one)
unique_warehouse_two = set(warehouse_two)

all_unique_products = unique_warehouse_one.union(unique_warehouse_two)
common_products = unique_warehouse_one.intersection(unique_warehouse_two)

print("Warehouse 1 unique:", unique_warehouse_one)
print("Warehouse 2 unique:", unique_warehouse_two)
print("All unique products:", all_unique_products)
print("Common products:", common_products)
