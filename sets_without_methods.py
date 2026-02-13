
# -----------------------------------
# Problem 1: Unique Numbers Without Set Methods
# Given a list of numbers with duplicates,
# create a set of unique numbers without using:
# add(), in, or any set methods.
# -----------------------------------

numbers = [3, 5, 3, 7, 8, 5, 9, 7]

unique_list = []

i = 0
while i < len(numbers):
    is_duplicate = False

    j = 0
    while j < len(unique_list):
        if numbers[i] == unique_list[j]:
            is_duplicate = True
            break
        j += 1

    if is_duplicate == False:
        unique_list.append(numbers[i])

    i += 1

unique_set = set()

k = 0
while k < len(unique_list):
    unique_set = unique_set | {unique_list[k]}
    k += 1

print("Unique set:", unique_set)
print("Unique count:", len(unique_set))


# -----------------------------------
# Problem 2: Common Users Without Set Methods
# Find common users between two lists
# without using:
# add(), in, union(), intersection(), difference()
# -----------------------------------

users_a = [101, 102, 103, 104, 105]
users_b = [103, 105, 106, 107]

common_list = []

i = 0
while i < len(users_a):
    j = 0
    while j < len(users_b):
        if users_a[i] == users_b[j]:
            common_list.append(users_a[i])
        j += 1
    i += 1

common_set = set()

k = 0
while k < len(common_list):
    common_set = common_set | {common_list[k]}
    k += 1

print("Common (raw list):", common_list)
print("Common (unique set):", common_set)

# -----------------------------------
# Problem 3: New Users Without Set Methods
# Find users who are in new_users but not in old_users
# without using:
# add(), in, union(), intersection(), difference()
# -----------------------------------

old_users = [1, 2, 3, 4]
new_users = [3, 4, 5, 6, 7]

result_list = []

i = 0
while i < len(new_users):
    j = 0
    found = False

    while j < len(old_users):
        if old_users[j] == new_users[i]:
            found = True
            break
        j += 1

    if not found:
        result_list.append(new_users[i])

    i += 1

result_set = set()
k = 0
while k < len(result_list):
    result_set = result_set | {result_list[k]}
    k += 1

print("New users (raw list):", result_list)
print("New users (unique set):", result_set)

# -----------------------------------
# Problem 4: Unique Products Without Set Methods
# Remove duplicates from a product list
# without using:
# add(), in, or any set methods
# -----------------------------------

products = [200, 201, 200, 202, 203, 201, 204]
unique_list = []

i = 0
while i < len(products):

    found = False
    j = 0

    while j < len(unique_list):
        if products[i] == unique_list[j]:
            found = True
            break
        j += 1

    if not found:
        unique_list.append(products[i])

    i += 1

unique_set = set()
k = 0
while k < len(unique_list):
    unique_set = unique_set | {unique_list[k]}
    k += 1

print("Unique products list:", unique_list)
print("Unique products set:", unique_set)


# -----------------------------------
# Problem 5: Username Check Without Set Methods
# Check if a username exists in a list
# without using:
# add(), in, or any set methods
# -----------------------------------

allowed_users = ["ali", "zara", "sami", "nora"]
username_to_check = "sami"

found = False
i = 0

while i < len(allowed_users):
    if allowed_users[i] == username_to_check:
        found = True
        break
    i += 1

if found:
    print("Username found")
else:
    print("Username not found")
