def days_to_units(num_of_days, conversion_unit):
    # conditional_check = num_of_days > 0
    # print(type(conditional_check))
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    # if user_input.isdigit():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculation_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number")

    except ValueError:
        print("you input is not a valid number")


user_input_message = "Hey user, enter number of days and I conversion unit!\n"
