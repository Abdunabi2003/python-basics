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