from itertools import groupby

test_cases = int(input("How many numbers do you want to test?: "))
accept_numbers = [input() for i in range (test_cases)]
accept_numbers = [case.split() for case in accept_numbers]

for each in range(test_cases):
    accept_numbers[each][1] = accept_numbers[each][1].split('-')

num = []

for obj, ele in accept_numbers:
    div = []
    for a in range(len(ele)):
        div.append(obj[0:int(ele[a])])
        obj = obj[int(ele[a]):]
    num.append(div)

interpret = ({'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', 
'6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}, 
{'':1, 'double':2, 'triple':3, 'quadruple':4, 'quintuple':5, 'sextuple':6, 'septuple':7, 'octuple':8, 'nonuple':9,
'decuple':10})

for count in range(test_cases):
    words = ''
    numer = [[''.join(g) for _, g in groupby(ele)] for ele in num[count]]
    for ele in numer:
        for each in ele:
            if len(each) < 2:
                words+=interpret[0].get(each[0], '') +' '
            else:
                words+=list(interpret[1].keys())[list(interpret[1].values()).index(len(each))]+' '
                words+=interpret[0].get(each[0], '')+ ' '
    print('Case #%d: %s' %(count+1,words))
