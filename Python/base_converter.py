#convert numbers from one base to another

from list_stack import Stack 

def base_converter(num,base):
    digits = "0123456789ABDCEF"
    remainder = Stack()
    while num > 0:
        rem = num % base
        remainder.push(rem)
        num = num // base

    string = " "
    while not remainder.empty_stack():
        string = string + digits[remainder.pop_item()]
    return string
num = int(input('Enter a number to be converted: '))
base = int(input("Conversion base: "))
print(base_converter(num,base))



