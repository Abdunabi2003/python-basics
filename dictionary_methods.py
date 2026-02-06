# Problem 1: Safe Access with get()
# Access a key safely using get(). If the key does not exist,
# return a default value instead of raising an error.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

result = thisdict.get("model", "Not found")
print(result)


# Problem 2: Keys & Values Summary
# Print all keys, values, and the total number of items in a dictionary.

scores = {
    "Ali": 85,
    "Vali": 90,
    "Zara": 78
}

print("Keys:", list(scores.keys()))
print("Values:", list(scores.values()))
print("Total items:", len(scores))

# Problem 3: Update Inventory
# Update stock values using update().

warehouse1 = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

warehouse2 = {
    "banana": 40,
    "orange": 25,
    "grape": 15
}

warehouse1.update(warehouse2)

print(warehouse1)

# Problem 4: Remove user safely with pop()

users = {
    "Ali": 25,
    "Vali": 30,
    "Zara": 22
}

users.pop("Zara", "Not found")
print(users)

# Problem 5: Remove last item from dictionary

users = {
    "Ali": 25,
    "Vali": 30,
    "Zara": 22
}

removed = users.popitem()

print("Updated users:", users)
print("Removed item:", removed)

# Problem 6: Copy and clear dictionary

users = {
    "Ali": 25,
    "Vali": 30,
    "Zara": 22
}

users_copy = users.copy()
users.clear()

print("Cleared users:", users)
print("Copied users:", users_copy)
