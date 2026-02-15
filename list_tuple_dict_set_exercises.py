# -----------------------------------
# Problem 1: Remove Duplicates from Sales
# A store recorded sold items during the day.
# Task: Find unique products and count them.
# -----------------------------------

sales = ["apple", "banana", "apple", "orange", "banana", "kiwi", "apple"]

unique_sales = set(sales)

print("Unique products sold:", unique_sales)
print("Number of unique products:", len(unique_sales))



# -----------------------------------
# Problem 2: Count Frequency of Exam Results
# Students received exam results.
# Task: Count how many times each result appears.
# -----------------------------------

results = ["pass", "fail", "pass", "pass", "fail", "pass", "fail"]

results_dict = {}
for result in results:
    if result in results_dict:
        results_dict[result] += 1
    else:
        results_dict[result] = 1

print(results_dict)


# -----------------------------------
# Problem 3: Filter Electronics Products
# An online shop has products and their categories.
# Task: Extract only products that belong to "electronics".
# -----------------------------------

products = {
    "laptop": "electronics",
    "phone": "electronics",
    "shirt": "clothing",
    "jeans": "clothing",
    "apple": "food"
}

electronics = set()
for product, category in products.items():
    if category == "electronics":
        electronics.add(product)

print(electronics)

# -----------------------------------
# Problem 4: Tuple to List Conversion
# A list of students is stored as a tuple.
# Task: Add a new student and convert back to tuple.
# -----------------------------------

students = ("Ali", "Vali", "Sami")

students = list(students)
students.append("Zara")
students = tuple(students)

print(students)

# -----------------------------------
# Problem 5: Users Registration Analysis
# Users registered on a website.
# Task: Find unique users, count registrations, and identify the most registered user(s).
# -----------------------------------

users = ["ali", "zara", "ali", "sami", "nora", "zara"]

# Unique users
unique_users = set(users)
print(unique_users)
print(len(unique_users))

# Count registrations
users_dict = {}
for user in users:
    if user in users_dict:
        users_dict[user] += 1
    else:
        users_dict[user] = 1
print(users_dict)

# Identify user(s) with maximum registrations
maximum = max(users_dict.values())
max_dict = {}
for user in users_dict:
    if users_dict[user] == maximum:
        max_dict[user] = users_dict[user]
print(max_dict)
