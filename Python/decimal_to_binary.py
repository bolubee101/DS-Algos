#aim: to convert decimal numbers(base 10 numbers) to binary(base 2 numbers)

from list_stack import Stack

def binary(decimal_num):
    remainder = Stack()
    while decimal_num > 0:
        rem = decimal_num % 2
        remainder.push(rem)
        decimal_num = decimal_num // 2
    
    binary_string = " "
    while not remainder.empty_stack():
         binary_string = binary_string + str(remainder.pop_item())
    return binary_string
decimal_num = int(input("Enter a number: "))
print(binary(decimal_num))