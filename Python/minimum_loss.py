
import random
import math
def min_loss(price):
    x = []
    #output = list(map(operator.sub, price,y))
    output = [price[i] - y[j] for i in range(len(price)-1) for j in range(len(y)-1)]
    for i in output:
         #print((output))
        if i > 0:
            #print(i)
            x.append(i)
    print(min(x))   
house_data = int(input('How many years is the house valid for: '))
price = list(map(int, input("price of house").rstrip().split()))
y = price[:]
random.shuffle(y)

min_loss(price)
