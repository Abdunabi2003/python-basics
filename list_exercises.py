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
