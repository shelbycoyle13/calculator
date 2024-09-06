def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt("Welcome to my calculator!")

# Ask the user for "number 1".
prompt("Please give me a number:")
num1 = input()

# Validate user input the first time
while invalid_number(num1):
    prompt("Hmm... that doesn't look like a valid number. Please try again.")
    num1 = input()

# Ask the user for "number 2".
prompt("Please give me one more number:")
num2 = input()

# Validate user input the second time
while invalid_number(num2):
    prompt("Hmm... that doesn't look like a valid number. Please try again.")
    num2 = input()

prompt(f"Okay, we have numbers {num1} and {num2}.")

# Ask the user what operation they want to perform:
# add, subtract, multiply or divide
prompt("""Would you like to
       1) add, 2) subtract, 3) multiply or 4) divide?""")
preference = input()

# Validate the user's operation input
while preference not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4:")
    preference = input()

# Perform the calculation using the 2 numbers
match preference:
    case "1":
        output = int(num1) + int(num2)
    case "2":
        output = int(num1) - int(num2)
    case "3":
        output = int(num1) * int(num2)
    case "4":
        output = int(num1) / int(num2)

# Output the result
prompt(f"The result is {output}.")
