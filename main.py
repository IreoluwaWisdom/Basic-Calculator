import string

# Initialize continue_ as True
continue_ = True

def accept_inputs():
    global continue_  # Access the global continue_ variable
    first_num = input('Please enter the first number:')
    
    if first_num == 'exit':
        continue_ = False  # Exit the program if 'exit' is entered
        return None

    if all(char in string.digits + '.' for char in first_num) and first_num.count('.') <= 1:
        first_num = float(first_num)
    else:
        print('Enter a valid number')
        return None

    second_num = input('Please enter the second number:')
    
    if second_num == 'exit':
        continue_ = False  # Exit the program if 'exit' is entered
        return None

    if all(char in string.digits + '.' for char in second_num) and second_num.count('.') <= 1:
        second_num = float(second_num)
    else:
        print('Enter a valid number')
        return None

    return first_num, second_num

def accept_sign():
    global continue_  # Access the global continue_ variable
    print('Please select operation')
    print('For addition enter the plus sign (+)\nFor subtraction, enter the minus sign (-)\nFor multiplication enter the times sign (*)\nFor division, enter the division sign (÷)')
    sign = input('')
    if sign == 'exit':
        continue_ = False  # Exit the program if 'exit' is entered
        return 'exit'  # Return 'exit' to indicate program exit
    return sign  # Return the selected operation sign

signs = ['+', '-', '×', '÷']

def calculator():
    global continue_  # Access the global continue_ variable
    inputs = accept_inputs()
    
    if inputs is not None:
        first_num, second_num = inputs
        sign = accept_sign()

        if continue_:
            result = calculate(first_num, second_num, sign)
            if result is not None:
                print('Result:', result)

def calculate(first_num, second_num, sign):
    if sign not in signs:
        print('Please input one of the available signs')
        return None
    if sign == '×':
        result = first_num * second_num
    elif sign == '÷':
        if second_num != 0:
            result = first_num / second_num
        else:
            print('The value is infinity')
            return None
    elif sign == '+':
        result = first_num + second_num
    elif sign == '-':
        result = first_num - second_num
    return result

# Run the calculator in a loop until continue_ becomes False
while continue_:
    calculator()
