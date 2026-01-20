# list_methods.py
# This file contains common list methods with simple examples.
# Topic: append, insert, pop, remove, sort, reverse

# append() - add item to the end of the list
numbers = [1, 2, 3]
numbers.append(4)
print("After append:", numbers)

# insert() - add item at a specific position
numbers.insert(1, 10)
print("After insert:", numbers)

# pop() - remove item by index
numbers.pop(2)
print("After pop:", numbers)

# remove() - remove item by value
numbers.remove(10)
print("After remove:", numbers)

# sort() - sort the list
scores = [88, 55, 92, 70]
scores.sort()
print("Sorted scores:", scores)

# reverse() - reverse list order
scores.reverse()
print("Reversed scores:", scores)
