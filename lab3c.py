#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''
# Author ID: JoyOtchere

def operate(number1, number2, operator):
    # Follow the operator's instructions to complete the process
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))        # The output expected: 15
    print(operate(10, 5, 'subtract'))   # The output expected: 5
    print(operate(10, 5, 'multiply'))   # The output expected: 50
    print(operate(10, 5, 'divide'))     # The output expected: Error message
