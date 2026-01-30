# tuples.py
# This file contains basic examples of working with Python tuples.
# Topic: creating tuples, accessing items, immutability, and looping.

# -----------------------------------
# Problem 1: Unique Elements Only
# Create a new tuple containing only
# elements that appear exactly once.
# The original order must be preserved.
# -----------------------------------

t = (1, 2, 10, 2, 3, 4, 4, 5, 10)
result = []

for item in t:
    if t.count(item) == 1:
        result.append(item)

print(tuple(result))


# -----------------------------------
# Problem 2: Most Frequent Element
# Find the element that occurs most
# frequently in a tuple. If multiple
# elements have the same highest
# frequency, return the first one.
# -----------------------------------

t = (1, 2, 2, 3, 3, 4)

max_count = 0
most_frequent = None

for item in t:
    count = t.count(item)
    if count > max_count:
        max_count = count
        most_frequent = item

print(most_frequent)


# -----------------------------------
# Problem 3: Tuple of Tuples – Max Values
# Given a tuple containing inner tuples
# of integers, create a new tuple
# consisting of the maximum value from
# each inner tuple.
# -----------------------------------

t = ((1, 5, 3), (10, 2), (7, 7, 7))
max_values = []

for inner in t:
    max_values.append(max(inner))

print(tuple(max_values))

# -----------------------------------
# Problem 4: Even and Odd Indices
# Given a tuple, split it into two tuples:
# - one containing elements at even indices
# - one containing elements at odd indices
# -----------------------------------

t = (10, 20, 30, 40, 50, 60)

even_index_elements = []
odd_index_elements = []

for idx, value in enumerate(t):
    if idx % 2 == 0:
        even_index_elements.append(value)
    else:
        odd_index_elements.append(value)

print(tuple(even_index_elements))
print(tuple(odd_index_elements))


# -----------------------------------
# Problem 5: Rotate a Tuple
# Given a tuple and an integer k,
# rotate the tuple to the right by k positions.
# -----------------------------------

t = (1, 2, 3, 4, 5)
k = 2 
k = k % len(t)

temp_list = list(t)
rotated = temp_list[-k:] + temp_list[:-k]

print(tuple(rotated))

# -----------------------------------
# Problem 6: Elements Between Min and Max
# Given a tuple of numbers, find the minimum
# and maximum values, and create a new tuple
# containing only the elements between them
# (excluding both).
# -----------------------------------

t = (-10, -5, -15, 2, 3, 4, 5, 20)

min_val = min(t)
max_val = max(t)
min_index = t.index(min_val)
max_index = t.index(max_val)

if min_index < max_index:
    between = t[min_index + 1:max_index]
else:
    between = t[max_index + 1:min_index]

print(tuple(between))

# -----------------------------------
# Problem 7: Tuple Equality (Without Sets)
# Check whether two tuples contain the
# same elements with the same frequencies,
# regardless of order.
# -----------------------------------

tuple1 = (1, 2, 2, 3, 1, 1, 1)
tuple2 = (2, 1, 3, 2, 1, 1, 3)

is_equal = True

if len(tuple1) != len(tuple2):
    is_equal = False
else:
    for i in tuple1:
        if tuple1.count(i) != tuple2.count(i):
            is_equal = False
            break

print(is_equal)



# -----------------------------------
# Problem 8: Longest String
# Find the longest string in a tuple.
# If multiple strings have the same
# maximum length, return the last one.
# -----------------------------------

t = ("car", "home", "tree", "book")

longest = ""

for word in t:
    if len(longest) <= len(word):
        longest = word

print(longest)


# -----------------------------------
# Problem 9: Nested Tuple Unpacking
# Unpack values from a nested tuple
# and calculate the average score.
# -----------------------------------

person, scores = ("Ali", (90, 85, 88))
average = sum(scores) / len(scores)
print(f"Name: {person}, Average score: {average}")


# -----------------------------------
# Problem 10: Candidate Filtering
# Filter candidates based on age
# and years of experience.
# -----------------------------------

candidates = (
    ("Ali", 22, 3),
    ("Vali", 20, 5),
    ("Sami", 25, 1),
    ("Zara", 23, 4)
)

qualified_candidates = []

for name, age, experience in candidates:
    if age > 21 and experience >= 2:
        qualified_candidates.append(name)

print(tuple(qualified_candidates))


# Problem 11
# Determine whether a sequence is increasing,
# decreasing, or mixed.

t = (1, 3, 2, 4)

increasing = True
decreasing = True

for i in range(len(t) - 1):
    if t[i] >= t[i + 1]:
        increasing = False
    if t[i] <= t[i + 1]:
        decreasing = False

if increasing:
    print("strictly increasing")
elif decreasing:
    print("strictly decreasing")
else:
    print("mixed")



# -----------------------------------
# Problem 12: Maximum Sum of Consecutive Elements
# Given a tuple of numbers, find the
# three consecutive elements with the
# maximum total sum.
# -----------------------------------

t = (1, 4, 2, 5, 6, 1, 7)

max_sum = sum(t[0:3])
max_triplet = t[0:3]

for i in range(1, len(t)-2):
    current = t[i:i+3]
    current_sum = sum(current)

    if current_sum > max_sum:
        max_sum = current_sum
        max_triplet = current

print(max_triplet)
print("Max sum:", max_sum)




