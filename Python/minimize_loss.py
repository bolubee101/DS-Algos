def minimize(price, n):
    bill = price[n:]
    if len(bill) <= 1:
        bill.clear()
        return bill
    else:
        loss = [bill[0]-m if (bill[0]-m) >= 0 else 0 for m in bill[1:]]
        loss = list(filter(lambda yay: yay != 0, loss))
        total = loss + minimize(bill[:], 1)
        return total
import sys
year = int(input('Number of years for house data: '))
cost = [int(ele) for ele in input('House price in each year: ').split()]
sys.setrecursionlimit(year) if year > 1000 else sys.setrecursionlimit(1000)
print(cost[0]) if len(cost) == 1 else print(min(minimize(cost[:],0)))