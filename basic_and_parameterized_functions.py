
# Simple functions
# -----------------------------------
# Problem 1: Print Even Numbers
# Task:
# Create a function that prints even numbers 
# from 1 to 20.
# -----------------------------------

def print_even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)


# Function call
print_even_numbers()

# -----------------------------------
# Problem 2: Find Maximum Number
# Task:
# Create a function that finds and prints 
# the largest number from the given list.
# -----------------------------------

def find_max_number():
    numbers = [12, 45, 7, 89, 23, 67]
    print("Maximum number:", max(numbers))


# Function call
find_max_number()

# -----------------------------------
# Problem 3: Print Word Lengths
# Task:
# Create a function that prints each word 
# and its length from the given list.
# -----------------------------------

def print_word_lengths():
    words = ["python", "code", "developer", "AI"]
    
    for word in words:
        print(f"{word} - {len(word)}")


# Function call
print_word_lengths()

# -----------------------------------
# Problem 4: Count Positive Numbers
# Task:
# Create a function that counts and prints 
# all positive numbers from the given list.
# -----------------------------------

def count_positive_numbers():
    numbers = [-5, 10, -3, 8, 0, 12, -1]
    
    print("Positive numbers:")
    
    for number in numbers:
        if number > 0:
            print(number)


# Function call
count_positive_numbers()

# -----------------------------------
# Problem 5: Check Palindrome
# Task:
# Create a function that checks whether 
# a given word is a palindrome.
# -----------------------------------

def check_palindrome():
    word = "level"
    
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


# Function call
check_palindrome()

# Functions with parameters

# -----------------------------------
# Problem 1: Power Calculator
# Task: Return base raised to the power of exponent
# -----------------------------------

def power_calculator(base, exponent):

    return base ** exponent


# Function call
result = power_calculator(2, 3)
print(result)

# -----------------------------------
# Problem 2: Name Formatter
# Task: Return full name in uppercase format
# -----------------------------------

def format_name(first_name, last_name):

    return f"{first_name.upper()} {last_name.upper()}"


# Function call
full_name = format_name("abdu", "karimov")
print(full_name)

# -----------------------------------
# Problem 3: Filter Long Words
# Task: Return words longer than given length
# -----------------------------------

def filter_long_words(words, length):

    filtered_words = []

    for word in words:
        if len(word) > length:
            filtered_words.append(word)

    return filtered_words


# Function call
words_list = ["apple", "banana", "kiwi", "strawberry"]
result = filter_long_words(words_list, 5)

print(result)

# -----------------------------------
# Problem 4: Count Vowels
# Task: Return the number of vowels in a word
# -----------------------------------

def count_vowels(word):

    vowels = {"a", "e", "i", "o", "u"}
    count = 0

    for char in word.lower():
        if char in vowels:
            count += 1

    return count


# Function call
result = count_vowels("AbduKarimova")
print(result)

# -----------------------------------
# Problem 5: Celsius to Fahrenheit Converter
# Task: Convert Celsius temperature to Fahrenheit
# -----------------------------------

def celsius_to_fahrenheit(celsius):

    return (celsius * 9 / 5) + 32


# Function call
result = celsius_to_fahrenheit(25)
print(result)