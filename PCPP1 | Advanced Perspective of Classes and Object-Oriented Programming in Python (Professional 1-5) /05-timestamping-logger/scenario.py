# Level of difficulty
#
# Medium
# Objectives
#
#     Improving the student's skills in creating decorators and operating with them.
#
# Scenario
#
#     Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
#     Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
#     Apply your decorator to those functions to ensure that the time of the function executions can be monitored.


import datetime

def timestamp_decorator(func):
    def wrapper(*args, **kwargs):
        print("[{}] Function '{}' started".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), func.__name__))
        result = func(*args, **kwargs)
        print("[{}] Function '{}' finished".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), func.__name__))
        return result
    return wrapper

@timestamp_decorator
def add_numbers(a, b):
    return a + b

@timestamp_decorator
def multiply_numbers(a, b):
    return a * b

print(add_numbers(2, 3))  # Output: [2023-06-30 14:26:42] Function 'add_numbers' started
                          #         [2023-06-30 14:26:42] Function 'add_numbers' finished
                          #         5
print(multiply_numbers(4, 5))  # Output: [2023-06-30 14:27:14] Function 'multiply_numbers' started
                               #         [2023-06-30 14:27:14] Function 'multiply_numbers' finished
                               #         20