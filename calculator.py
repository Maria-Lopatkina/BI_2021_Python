'''Using sys.exit() for calculator finishing'''
import sys


def number_check():
    '''In a case of the type of var is 'float', function returns float(var)'''
    var = input("Enter a number: ")
    if var == 'stop':
        sys.exit()
    count = 0
    while count != 1:
        try:
            float(var)
            return float(var)
        except ValueError:
            print("The \"", var, "\" is not a number")
            var = input("Enter a number: ")
            if var == 'stop':
                sys.exit()


def operator_check():
    '''Function checks the correctness of the entered operator'''
    var = input("Enter an operator: ")
    if var == 'stop':
        sys.exit()
    count = 0
    while count != 1:
        if var in ('+', '-', '*', '/', '//', '%', '**'):
            return var
        print("The \"", var, "\" is not an operator.")
        var = input("Enter an operator: ")
        if var == "stop":
            sys.exit()


print("Hello, stranger! It is a simple calculator for:\n"
      "addition (+)\nsubtraction (-)\nmultiplication (*)\ndivision (/)\n"
      "floor division (//)\nmodular division (%)\nexponentiation (**)\n"
      "For finishing the script print 'stop' (without quotes).\n")
number_1 = number_check()
operator = operator_check()
number_2 = number_check()
while number_2 == 0 and operator in ('/', '//', '%'):
    print('Division by zero!')
    number_1 = number_check()
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
