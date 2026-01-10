# type_conversion.py

# int to float
a = 10
print("10 converted to float:", float(a))

# float to int
b = 10.8
print("10.8 converted to int:", int(b))

# int to string
c = 25
print("25 converted to string:", str(c))
print("Type after conversion:", type(str(c)))

# string to int
d = "40"
print("'40' converted to int:", int(d))

# string to float
e = "3.14"
print("'3.14' converted to float:", float(e))

# boolean conversions
print("1 to bool:", bool(1))
print("0 to bool:", bool(0))

print("Empty string to bool:", bool(""))
print("Non-empty string to bool:", bool("Python"))

# list and tuple
numbers_list = [1, 2, 3]
print("List to tuple:", tuple(numbers_list))

numbers_tuple = (4, 5, 6)
print("Tuple to list:", list(numbers_tuple))
