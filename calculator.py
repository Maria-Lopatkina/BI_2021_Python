import sys


def number_check():
    x = input("Enter a number: ")
    if x == 'stop':
        sys.exit()
    z = 0
    while z != 1:
        try:
            float(x)
            return float(x)
        except ValueError:
            print("The \"", x, "\" is not a number")
            x = input("Enter a number: ")
            if x == 'stop':
                sys.exit()


def operator_check():
    x = input("Enter an operator: ")
    if x == 'stop':
        sys.exit()
    z = 0
    while z != 1:
        if x == "+" or x == "-" or x == "*" or x == "/" or x == "//" or x == "%" or x == "**":
            return x
        else:
            print("The \"", x, "\" is not an operator. The operation cannot be performed")
            x = input("Enter an operator: ")
            if x == "stop":
                sys.exit()


print("Hello, stranger! It is a simple calculator. Note, that the possible operators are:\n"
      "addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modular division (%), "
      "and exponentiation (**)\nFor finishing the script print 'stop' (without quotes).")
number_1 = number_check()
operator = operator_check()
number_2 = number_check()
while number_2 == 0 and (operator == '/' or operator == '//' or operator == '%'):
    print('Division by zero!')
    number1 = number_check()
    operator = operator_check()
    number_2 = number_check()
if operator == '+':
    print("Result is", number_1 + number_2)
elif operator == '-':
    print("Result is", number_1 - number_2)
elif operator == '*':
    print("Result is", number_1 * number_2)
elif operator == '/':
    print("Result is", number_1 / number_2)
elif operator == '//':
    print("Result is", number_1 // number_2)
elif operator == '%':
    print("Result is", number_1 % number_2)
elif operator == '**':
    print("Result is", number_1 ** number_2)
