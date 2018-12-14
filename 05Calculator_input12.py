def input_first_int():
    number1_str = input(" First number: ")
    number1 = int(number1_str)
    return number1


def input_second_int():
    number2_str = input("Second number: ")
    number2 = int(number2_str)
    return number2


def output(parameter1, parameter2):
    parameter1_str = str(parameter1)
    parameter2_str = str(parameter2)
    print(parameter1_str + parameter2_str)


number1 = input_first_int()

number2 = input_second_int()

operation = input("Operation [+, -]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2

output("Answer: ", combination)

print()
input("Press return to continue ...")
