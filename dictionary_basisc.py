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
