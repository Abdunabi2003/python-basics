# list_exercises.py
# This file contains real-world practice problems using Python lists.
# Focus: lists, loops, and conditions.

# -----------------------------------
# Problem 1:
# A shop has a list of daily sales amounts.
# Calculate the total sales for the day.
# -----------------------------------

sales = [1, 2, 3, 4, 5]

total_sales = 0
for sale in sales:
    total_sales += sale

print("Total sales:", total_sales)

# -----------------------------------
# Problem 2:
# A company stores employee salaries in a list.
# Find and print the highest salary.
# Do not use the built-in max() function.
# -----------------------------------

a = [-5, 1, 2, 3, 4, 51, 6, 100]

maksimal = a[0]
for i in range(1, len(a)):
    if a[i] > maksimal:
        maksimal = a[i]

print(maksimal)


# -----------------------------------
# Problem 3:
# A system stores user ages in a list.
# Count how many users are adults (18 or older)
# and how many are under 18.
# -----------------------------------

ages = [18, 19, 22, 16, 15, 14, 12]

adults = 0
minors = 0
exact_18 = 0

for age in ages:
    if age == 18:
        exact_18 += 1
    elif age > 18:
        adults += 1
    else:
        minors += 1

print("Exactly 18:", exact_18)
print("Adults:", adults)
print("Under 18:", minors)



# -----------------------------------
# Problem 4:
# A store has a list of product prices.
# Create a new list that contains only the prices
# greater than 100,000.
# -----------------------------------

prices = [100, 200, 3, 4, 500, 6, 7, 8000000, 900000]
expensive_prices = []

for price in prices:
    if price > 100000:
        expensive_prices.append(price)

print(expensive_prices)


# -----------------------------------
# Problem 5:
# A customer has a list of product prices in their cart.
# Calculate the total price.
# If the total exceeds 1,000,000,
# apply a 10% discount and print the final amount.
# -----------------------------------
prices = [1, 2, 3000000, 4, 5000000]

total = 0
for price in prices:
    total += price

if total > 1000000:
    final_price = total - total * 0.10
    print("Discount applied:", final_price)
else:
    print("Total price:", total)

# -----------------------------------
# Problem 6:
# A system stores user IDs in a list.
# Some IDs may be duplicated.
# Create a new list that contains only unique IDs
# while keeping the original order.
# -----------------------------------

user_ids = [101, 203, 101, 405, 203, 507,507]
new_user_ids = []
for i in user_ids:
    if i not in new_user_ids:
        new_user_ids.append(i)
print(new_user_ids)

# -----------------------------------
# Problem 7:
# Given a list of numbers,
# find and print the second largest number.
# Do not use built-in sorting functions.
# -----------------------------------

numbers = [50, 3, 0, 30, 40, 11, 70, 60, 70, 60, 1, 9, 5, 10, -5, 15, 20]

max_number = numbers[0]

# Find the maximum number
for num in numbers:
    if num > max_number:
        max_number = num

# Find the second maximum
second_max = None
for num in numbers:
    if num != max_number:
        if second_max is None or num > second_max:
            second_max = num

print("Second largest number:", second_max)

# -----------------------------------
# Problem 8:
# A shop stores daily sales amounts in a list.
# Calculate the total sales.
# Then calculate and print the average sale value.
# -----------------------------------

sales = [120, 150, 100, 130, 170]
s = 0

for i in range(len(sales)):
    s += sales[i]

if len(sales) > 0:
    print(s / len(sales))


# -----------------------------------
# Problem 9:
# Given a list of integers,
# check whether the list is sorted in ascending order.
# Print True if it is sorted, otherwise print False.
# -----------------------------------

t_numbers = [-6, 1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(t_numbers) - 1):
    if t_numbers[i] > t_numbers[i + 1]:
        is_sorted = False
        break

print(is_sorted)


# -----------------------------------
# Problem 10:
# Given a list of numbers,
# reverse the list without using reverse() or slicing.
# -----------------------------------
numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)
