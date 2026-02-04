# -----------------------------------
# Problem 1: Word Frequency
# Given a list of words, create a dictionary
# where keys are words and values are how many
# times each word appears.
# The original order of first appearance
# should be preserved.
# -----------------------------------

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)


# -----------------------------------
# Problem 2: Student Grades Summary
# Given a dictionary of students and their
# list of grades, create a new dictionary
# with the student's name as key and their
# average grade as value.
# -----------------------------------

students = {
    "Ali": [90, 85, 88],
    "Vali": [70, 75, 80],
    "Zara": [95, 100, 98]
}

avg_grades = {}

for student in students:
    avg_grades[student] = sum(students[student]) / len(students[student])

print(avg_grades)

# -----------------------------------
# Problem 3: Invert Dictionary (With Duplicates)
# Given a dictionary where values may repeat,
# create a new dictionary where:
# - keys become values
# - values become lists of keys
# Example:
# {"a": 1, "b": 2, "c": 1}
# Result:
# {1: ["a", "c"], 2: ["b"]}
# -----------------------------------

one_dictionary = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 3}
two_dictionary = {}

for key in one_dictionary:
    value = one_dictionary[key]

    if value not in two_dictionary:
        two_dictionary[value] = []

    two_dictionary[value].append(key)

print(two_dictionary)


# -----------------------------------
# Problem 4: Merge Dictionaries with Priority
# Given two dictionaries with possible overlapping keys,
# merge them into one dictionary.
# If the same key exists in both,
# keep the value from the second dictionary.
# -----------------------------------

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print(merged)

# -----------------------------------
# Problem 5: Most Frequent Value
# Given a dictionary, find the value
# that appears most frequently.
# If multiple values have the same highest frequency,
# return the one whose key appears first
# in the original dictionary.
# -----------------------------------

d = {"a": 5, "b": 6, "c": 5, "d": 6}

freq = {}
max_count = 0
most_frequent_value = None

for key in d:
    value = d[key]

    freq[value] = freq.get(value, 0) + 1

    if freq[value] > max_count:
        max_count = freq[value]
        most_frequent_value = value

print(most_frequent_value)


# Problem 6: Filter by Value Range
# Keep students with scores between 70 and 90 (inclusive).

students = {
    "Ali": 85,
    "Fali": 90,
    "Varvara": 60,
    "Vali": 70,
    "Zara": 50,
}

filtered_students = {}

for name, score in students.items():
    if 70 <= score <= 90:
        filtered_students[name] = score

print(filtered_students)

# Problem 7: Swap Keys and Values (Handle Duplicates)
# Group keys by their values.

numbers = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 3, "f": 4}

grouped = {}

for key, value in numbers.items():
    if value not in grouped:
        grouped[value] = []
    grouped[value].append(key)

print(grouped)

# Problem 8: Top Scorer
# Find the student with the highest score.
# If multiple students have the same highest score,
# return the first one encountered.

students = {
    "Ali": 85,
    "Fali": 90,
    "Varvara": 60,
    "Vali": 70,
    "Zara": 90,
}

max_score = None
top_student = None

for name, score in students.items():
    if max_score is None or score > max_score:
        max_score = score
        top_student = name

print(top_student, max_score)

# Problem 9: Merge and Sum Values
# Merge two dictionaries. If a key exists in both,
# sum their values.

dict1 = {"a": 2, "b": 3}
dict2 = {"b": 5, "c": 1}

result = {}

for key, value in dict1.items():
    result[key] = value

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)

# Problem 10: Remove Zero Values
# Create a new dictionary without keys that have value 0.

data = {"a": 3, "b": 0, "c": 5, "d": 0}

filtered_data = {}

for key, value in data.items():
    if value != 0:
        filtered_data[key] = value

print(filtered_data)

