LANGUAGE = "es"

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang="en"):
    return MESSAGES[lang][message]

def prompt(key, **kwargs):
    message = messages(key, LANGUAGE)

    if kwargs:
        message = message.format(**kwargs)

    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

while True:
    prompt("welcome")

    # Ask the user for "number 1".
    prompt("ask_first_number")
    num1 = input()

    # Validate user input the first time
    while invalid_number(num1):
        prompt("invalid_number")
        num1 = input()

    # Ask the user for "number 2".
    prompt("one_more_number")
    num2 = input()

    # Validate user input the second time
    while invalid_number(num2):
        prompt("invalid_number")
        num2 = input()

    prompt("stating_numbers", num1=num1, num2=num2)

    # Ask the user what operation they want to perform:
    # add, subtract, multiply or divide
    prompt("ask_operation")
    operation = input()

    # Validate the user's operation input
    while operation not in ["1", "2", "3", "4"]:
        prompt("operation_choice")
        operation = input()

    # Perform the calculation using the 2 numbers
    match operation:
        case "1":
            output = float(num1) + float(num2)
        case "2":
            output = float(num1) - float(num2)
        case "3":
            output = float(num1) * float(num2)
        case "4":
            output = float(num1) / float(num2)

    # Output the result
    prompt("result", output=output)

    # Ask the user if they want to perform another calculation
    prompt("another_calculation")
    preference = input()

    # Validate user's preference
    while preference not in ["Y", "y", "N", "n"]:
        prompt("preference_choice")
        preference = input()
    
    # Exit if user wants to stop
    if preference in ["N", "n"]:
        prompt("end_of_program")
        break