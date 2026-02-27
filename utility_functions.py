"""
Project: Advanced Calculator

This function performs basic mathematical operations
(sum, max, min, average) on a variable number of numbers.

Parameters:
    operation (str): "sum", "max", "min", or "average"
    *numbers: unlimited numeric values
    round_result (bool, optional): round the result if True

Returns:
    tuple:
        - result of the operation
        - number of values processed

Raises:
    ValueError: if no numbers are provided or operation is invalid
"""


def advanced_calculator(operation, *numbers, round_result=False):
    if not numbers:
        raise ValueError("At least one number must be provided.")

    operation = operation.lower()

    if operation == "sum":
        result = sum(numbers)
    elif operation == "max":
        result = max(numbers)
    elif operation == "min":
        result = min(numbers)
    elif operation == "average":
        result = sum(numbers) / len(numbers)
    else:
        raise ValueError("Invalid operation. Use 'sum', 'max', 'min', or 'average'.")

    if round_result:
        result = round(result)

    return result, len(numbers)


# Simple usage example
result, count = advanced_calculator("average", 10, 20, 30, 40, round_result=True)

print("Result:", result)
print("Numbers processed:", count)



"""
Project: Student Performance Analyzer

This function analyzes a student's scores using *args.
It calculates the average, highest, and lowest score
after applying an optional bonus to each score.

Parameters:
    name (str): student's name
    *scores: unlimited numeric scores
    bonus (int | float, optional): bonus points added to each score

Returns:
    tuple:
        - student name
        - average score
        - highest score
        - lowest score

Raises:
    ValueError: if no scores are provided
"""


def student_performance(name, *scores, bonus=0):
    if not scores:
        raise ValueError("At least one score must be provided.")

    adjusted_scores = []

    for score in scores:
        adjusted_scores.append(score + bonus)

    average_score = sum(adjusted_scores) / len(adjusted_scores)
    highest_score = max(adjusted_scores)
    lowest_score = min(adjusted_scores)

    return name, average_score, highest_score, lowest_score


# Simple usage example
student, avg, high, low = student_performance("Abdu", 10, 15, 20, bonus=15)

print("Student:", student)
print("Average score:", avg)
print("Highest score:", high)
print("Lowest score:", low)



"""
Project: Number Statistics

This function analyzes numbers using conditional statements.
It counts even or odd numbers based on the check_even parameter
and returns statistical information.

Parameters:
    *numbers: unlimited integer values
    check_even (bool, optional):
        True  -> count even numbers
        False -> count odd numbers

Returns:
    tuple:
        - count of selected numbers
        - maximum number
        - minimum number
        - sum of all numbers

Raises:
    ValueError: if no numbers are provided
"""


def number_statistics(*numbers, check_even=True):
    count = 0

    if not numbers:
        raise ValueError("At least one number must be provided.")

    elif check_even:
        for number in numbers:
            if number % 2 == 0:
                count += 1

    else:
        for number in numbers:
            if number % 2 != 0:
                count += 1

    return count, max(numbers), min(numbers), sum(numbers)


# Simple usage example
result = number_statistics(1, 2, 3, 4, 5, 6, check_even=False)

print("Result:", result)



"""
Project: Shopping Cart System

This function calculates the total purchase amount,
applies discount and tax, and returns a summary dictionary.

Parameters:
    customer_name (str): name of the customer
    *prices: unlimited product prices
    discount (float, optional): discount percentage
    tax (float, optional): tax percentage

Returns:
    dict:
        {
            "customer_name": str,
            "original_total": float,
            "final_total": float
        }

Raises:
    ValueError: if no prices are provided
"""


def shopping_cart(customer_name, *prices, discount=0, tax=0):
    if not prices:
        raise ValueError("At least one price must be provided.")

    original_total = sum(prices)

    discount_amount = original_total * (discount / 100)
    discounted_total = original_total - discount_amount

    tax_amount = discounted_total * (tax / 100)
    final_total = discounted_total + tax_amount

    user = {
        "customer_name": customer_name,
        "original_total": original_total,
        "final_total": final_total,
    }

    return user


# Simple usage example
result = shopping_cart("Ali", 100, 200, discount=10, tax=5)

print(result)


"""
Project: Text Processor

This function processes multiple words using optional transformations.
It can convert words to uppercase, sort them alphabetically,
and return useful text statistics.

Parameters:
    *words: unlimited string inputs
    upper (bool, optional): convert words to uppercase if True
    sort_words (bool, optional): sort words alphabetically if True

Returns:
    tuple:
        - processed word list
        - total number of words
        - longest word
        - shortest word
        - combined text sentence

Raises:
    ValueError: if no words are provided
"""


def text_processor(*words, upper=False, sort_words=False):
    if not words:
        raise ValueError("At least one word must be provided.")

    processed_words = list(words)

    if upper:
        processed_words = [w.upper() for w in processed_words]

    if sort_words:
        processed_words.sort()

    text = " ".join(processed_words)

    total_words = len(processed_words)
    longest_word = max(processed_words, key=len)
    shortest_word = min(processed_words, key=len)

    return processed_words, total_words, longest_word, shortest_word, text


# Simple usage examples
print(text_processor("python", "is", "very", "powerful"))
print(text_processor("python", "is", "very", "powerful", upper=True))
print(text_processor("python", "is", "very", "powerful", sort_words=True))
print(text_processor("python", "is", "very", "powerful", upper=True, sort_words=True))