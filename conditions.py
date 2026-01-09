#conditions.py

age=20

if age >=18:
    print("You are an adult.")
else:
    print("You are under 18.")


score=85

if score>=90:
    print("Grade: A")
elif score >=75:
    print("Grade: B")
else:
    print("Grade: C")


# Example: Student score evaluation
# Problem:
# Write a program that takes a student's score (0–100)
# and prints the corresponding grade using if-elif-else.

score=int(input("Enter score: "))

if score>100 or score<0:
    print("Invalid score")
elif score>=90:
    print("Excellent")
elif 75<=score<=89:
    print("Good")
elif 60<=score<=74:
    print("Satisfactory")
elif 50<=score<=59:
    print("Pass")
elif score<50:
    print("Fail")



# Problem:
# A bank checks a loan application based on:
# - age (must be 21 or older)
# - monthly salary (must be at least 3,000,000)
# - credit history (must be "good")
# Print the loan decision.

age=int(input("Enter age: "))
salary=int(input("Enter monthly salary: "))
credit_history=input("Enter credit history (good/bad): ").lower()

if age<21:
    print("Rejected: applicant is under 21")
elif salary<3000000:
    print("Rejected: insufficient salary")
elif credit_history!="good":
    print("Rejected: bad credit history")
else:
    print("Credit approved")



# Problem:
# A customer gets a discount based on:
# - purchase amount
# - loyalty card (1 = yes, 0 = no)

amount = int(input("Enter purchase amount: "))
loyalty_card = input("Do you have a loyalty card? (1 = yes, 0 = no): ")

if amount >= 1_000_000 and loyalty_card == "1":
    final_price = amount - amount * 0.20
    print("20% discount applied. You pay:", final_price)

elif amount >= 1_000_000 and loyalty_card == "0":
    final_price = amount - amount * 0.10
    print("10% discount applied. You pay:", final_price)

elif 500_000 <= amount < 1_000_000:
    final_price = amount - amount * 0.05
    print("5% discount applied. You pay:", final_price)

else:
    print("No discount. You pay:", amount)




# Problem:
# Determine traffic penalty based on speed limit violation.

speed_limit = int(input("Enter speed limit: "))
actual_speed = int(input("Enter actual speed: "))

difference = actual_speed - speed_limit

if actual_speed <= 0:
    print("Invalid speed")

elif 1 <= difference <= 10:
    print("Warning")

elif 11 <= difference <= 30:
    print("Fine")

elif difference > 30:
    print("Heavy fine")

else:
    print("No violation")




# Problem:
# Check user login based on username, password, and account status.

username_input = input("Enter username: ")
password_input = input("Enter password: ")
status = input("Enter account status (active/blocked): ").lower()

correct_username = "ali"
correct_password = "vali"

if status == "blocked":
    print("Account is blocked")

elif username_input != correct_username or password_input != correct_password:
    print("Invalid credentials")

else:
    print("Login successful")
