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

