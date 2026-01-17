#loops.py
# This file contains examples of loops in Python
# Topic: for loop, while loop, break, continue


# Example 1:
# Print numbers from 1 to 20.
# If the number is a multiple of 5,
# print "multiple of 5" next to the number.


for i in range(1, 21):
    if i % 5 == 0:
        print(f"{i} - multiple of 5")
    else:
        print(i)


# Example 2:
# Ask the user to enter a number.
# Calculate and print the sum of all even numbers
# from 1 up to the entered number.


number = int(input("Enter a number: "))
total = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)


# Example 3:
# There are 5 products in a shop.
# Ask the user to enter the price of each product.
# Calculate the total amount.
# If the total is greater than 1,000,000,
# print "Discount available".

products = ["apple", "quince", "peach", "cherry", "sour cherry"]
total = 0
for i in range(len(products)):
    price = int(input(f"Enter price for {products[i]}: "))
    total += price

if total > 1_000_000:
    print("Discount available")
else:
    print("Total amount:", total)


# Example 4:
# Print all numbers from 1 to 100
# that are divisible by both 3 and 5.
# Also print how many such numbers were found.

count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        count += 1

print("Total:", count)


# Example 5:
# Ask the user to enter a number.
# Print the multiplication table for this number
# from 1 to 10 in the format:
# number x i = result

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# WHILE LOOP EXAMPLES

# Example 1:
# The user enters a number.
# If the number is positive, print numbers from 1 to that number.
# If the number is negative, print numbers from 1 down to that number.
a = int(input("Enter a number: "))
if a > 0:
    i = 1
    while i <= a:
        print(i)
        i += 1
elif a < 0:
    i = 1
    while i >= a:
        print(i)
        i -= 1
else:
    print("You entered zero")



# Example 2:
# The user enters a number.
# Calculate the sum of all numbers
# from 1 to the entered number using a while loop.
# Works for both positive and negative numbers.
a = int(input("Enter a number: "))
total = 0
if a > 0:
    i = 1
    while i <= a:
        total += i
        i += 1
elif a < 0:
    i = 1
    while i >= a:
        total += i
        i -= 1
else:
    total = 0
print("Sum:", total)


# Example 3:
# Keep asking the user to enter numbers.
# Add all entered numbers.
# Stop when the user enters 0.
# Then print the total sum.

total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number

print("Sum:", total)

# Example 4:
# Ask the user to enter a password.
# Keep asking until the correct password is entered.
# When the password is correct, grant access.
correct_password = "python123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break

# Example 5:
# Ask the user to enter an integer.
# Print how many digits the number has.
# Negative numbers should also be handled.

number = int(input("Enter a number: "))
if number == 0:
    print(1)
else:
    number = abs(number)
    count = 0
    while number > 0:
        number //= 10
        count += 1
    print(count)