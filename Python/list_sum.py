#add numbers in a list

#for loop

def list_sum(num):
    sum_of_num = 0
    for i in num:
        sum_of_num += i
    print(sum_of_num)
sum_of_num = [1,2,3,4,5,6,7,8,9,10]
list_sum(sum_of_num)

#if statements
def sum_list(num):
    if len(num) == 1:
        return (num[0])
    else:
        return (num[0] + sum_list(num[1:]))
num = [1,2,3,4,5,6,7,8,9,10]
print(sum_list(num))
