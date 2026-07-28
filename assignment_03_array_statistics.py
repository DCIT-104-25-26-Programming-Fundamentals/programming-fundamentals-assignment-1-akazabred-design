# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =================================================================


def sum_of_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def average_of_numbers(numbers):
    total = sum_of_numbers(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

def maximum_of_numbers(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

def minimum_of_numbers(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for n in numbers:
        if n < min_num:
            min_num = n
    return min_num