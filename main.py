'''print("20 days are " + str(50) + " minutes")
print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"35 days are {35 * calculation_to_units} {name_of_unit} ")
print(f"50 days are {50 * calculation_to_units} {name_of_unit}")
print(f"110 days are {110 * calculation_to_units} {name_of_unit}")'''

"""def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print("All good!")


days_to_units(20, "Awesome!")
days_to_units(35, "Looks good!")


def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)


scope_check(20)"""
#import helper as h

from helper import validate_and_execute, user_input_message
"""import logging

logger = logging.getLogger("main")
logger.error("Error happened in the app")"""

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)
