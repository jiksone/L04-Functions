def input_int(prompt):
    string = input(prompt)
    number = int(string)
    return number


def calculate(number1, number2, operation):
    if operation == "+":
        combination = number1 + number2
    elif operation == "-":
        combination = number1 - number2
    return combination


def output(parameter1, parameter2):
    parameter1_str = str(parameter1)
    parameter2_str = str(parameter2)
    print(parameter1_str + parameter2_str)


number1 = input_int(" First number: ")

number2 = input_int("Second number: ")

operation = input("Operation [+, -]: ")

combination = calculate(number1, number2, operation)

output("Answer: ", combination)

print()
input("Press return to continue ...")
