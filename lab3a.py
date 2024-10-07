#!/usr/bin/env python3


# return_text_value() function
# Author ID: JoyOtchere

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting


# return_number_value() function

def return_number_value():
    number = 15  
    return number


# Main Program


if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))


