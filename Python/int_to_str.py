#convert an integer to a string in base 10

def int_to_str(num,base):
    conversion = '0123456789ABDCEF'
    if num < base:
        return conversion[num]
    else:
        return int_to_str(num / base, base) + conversion[num % base]
num = 1453
base = 16
print(int_to_str(1456,16))


