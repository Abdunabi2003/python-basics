"""
Project: Smart Order System

This function processes a customer's order by calculating the
original total, applying a discount, adding tax, and storing
additional customer information.

Function:
    process_order(customer_name, *items, discount=0, tax=0, **extra_info)

Parameters:
    customer_name (str): name of the customer
    *items (int | float): product prices
    discount (float): discount percentage
    tax (float): tax percentage
    **extra_info: additional customer information

Returns:
    dict:
        customer_name
        number_of_items
        original_total
        final_total
        extra_info
"""


def process_order(customer_name, *items, discount=0, tax=0, **extra_info):
    if not items:
        raise ValueError("No items provided.")

    total = 0
    valid_items = 0

    for item in items:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            total += item
            valid_items += 1

    original_total = total

    discount_amount = original_total * discount / 100
    discount_total = original_total - discount_amount

    tax_amount = discount_total * (tax / 100)
    final_total = discount_total + tax_amount

    return {
        "customer_name": customer_name,
        "number_of_items": valid_items,
        "original_total": original_total,
        "final_total": final_total,
        "extra_info": extra_info,
    }


# Example usage
order = process_order(
    "Ali",
    10000, 20000, 15000,
    discount=10,
    tax=5,
    phone="998901234567",
    city="Tashkent"
)

print(order)


"""
Project: Advanced Student Report

This function evaluates a student's performance by
adjusting grades with a bonus, calculating the average,
and determining the academic status.

Function:
    student_report(name, *grades, bonus=0, **details)

Parameters:
    name (str): student's name
    *grades (int | float): student grades
    bonus (int | float): bonus points added to each grade
    **details: additional student information

Returns:
    dict:
        student_name
        average_score
        status
        details
"""


def student_report(name, *grades, bonus=0, **details):
    k = []

    if not grades:
        raise ValueError("Grades cannot be empty")

    for grade in grades:
        if isinstance(grade, (int, float)) and not isinstance(grade, bool):
            k.append(grade + bonus)

    if not k:
        raise ValueError("No valid grades")

    average = sum(k) / len(k)

    if average >= 90:
        status = "Excellent"
    elif average >= 75:
        status = "Good"
    elif average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    return {
        "student_name": name,
        "average_score": average,
        "status": status,
        "details": details,
    }


# Example usage
report = student_report(
    "Abdu",
    85, 78, 92,
    bonus=5,
    age=21,
    university="TUIT"
)

print(report)



"""
Project: Flexible Data Analyzer

This function analyzes numbers dynamically by filtering them
based on a selected mode and returning statistical information.

Function:
    data_analyzer(*numbers, mode="even", **config)

Modes:
    "even"      -> analyze even numbers
    "odd"       -> analyze odd numbers
    "positive"  -> analyze positive numbers
    "negative"  -> analyze negative numbers

Parameters:
    *numbers (int | float): numbers to analyze
    mode (str): filtering mode
    **config: additional configuration options

Returns:
    dict:
        count
        maximum
        minimum
        total
        average
        config
"""


def data_analyzer(*numbers, mode="even", **config):
    filtered = []

    if not numbers:
        raise ValueError("Numbers cannot be empty")

    for number in numbers:
        if isinstance(number, (int, float)) and not isinstance(number, bool):

            if mode == "even":
                if number % 2 == 0:
                    filtered.append(number)

            elif mode == "odd":
                if number % 2 != 0:
                    filtered.append(number)

            elif mode == "positive":
                if number > 0:
                    filtered.append(number)

            elif mode == "negative":
                if number < 0:
                    filtered.append(number)

            else:
                raise ValueError("Invalid mode")

    if not filtered:
        raise ValueError("No numbers found for this mode")

    count = len(filtered)
    maximum = max(filtered)
    minimum = min(filtered)
    total = sum(filtered)
    average = total / count

    return {
        "count": count,
        "maximum": maximum,
        "minimum": minimum,
        "total": total,
        "average": average,
        "config": config,
    }


# Example usage
result = data_analyzer(
    10, 15, -5, 8, 20, -3,
    mode="even",
    source="sensor_A"
)

print(result)




"""
Project: Dynamic Text Formatter

This function formats text dynamically using optional transformations.

Function:
    text_formatter(*words, upper=False, reverse=False, **options)

Features:
- Convert words to uppercase.
- Reverse word order.
- Join words using a custom separator.
- Optionally add an exclamation mark.

Parameters:
    *words (str): words to format
    upper (bool): convert words to uppercase
    reverse (bool): reverse word order
    **options:
        separator (str) -> word separator (default: space)
        add_exclamation (bool) -> add "!" at the end

Returns:
    tuple:
        formatted_text
        statistics dictionary
"""


def text_formatter(*words, upper=False, reverse=False, **options):
    list_words = []
    words = list(words)

    for word in words:
        if upper:
            list_words.append(word.upper())
        else:
            list_words.append(word)

    if reverse:
        list_words.reverse()

    word_count = len(list_words)
    longest_word = max(list_words, key=len)
    shortest_word = min(list_words, key=len)

    separator = options.get("separator", " ")

    text = separator.join(list_words)

    if options.get("add_exclamation"):
        text += "!"

    return text, {
        "word_count": word_count,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "separator": separator,
    }


# Example usage
formatted_text, stats = text_formatter(
    "python", "is", "awesome",
    upper=True,
    reverse=True,
    separator="-",
    add_exclamation=True
)

print(formatted_text)
print(stats)


"""
Project: Employee Payroll System

This function calculates an employee's salary by adding bonuses
to the base salary and applying tax deductions.

Function:
    calculate_salary(name, base_salary, *bonuses, tax=0, **info)

Parameters:
    name (str): employee name
    base_salary (int | float): base salary amount
    *bonuses (int | float): additional bonus payments
    tax (float): tax percentage
    **info: additional employee information

Returns:
    dict:
        name
        gross_salary
        net_salary
        info
"""


def calculate_salary(name, base_salary, *bonuses, tax=0, **info):
    gross_salary = base_salary + sum(bonuses)

    tax_amount = gross_salary * tax / 100
    net_salary = gross_salary - tax_amount

    return {
        "name": name,
        "gross_salary": gross_salary,
        "net_salary": net_salary,
        "info": info,
    }


# Example usage
salary = calculate_salary(
    "Ali",
    1000,
    200, 150,
    tax=10,
    department="IT",
    experience=5
)

print(salary)