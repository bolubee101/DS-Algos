'''
SUPER DIGIT: gotten from the recursive sum of individual numbers
function name: superdigit
n = string rep of an integer
k = an integer representing the  number of concatenation
p = single super digit gotten from adding individual digits of n
'''
def recurse(digit_sum_y):
	while True:
		#print(digit_sum_y)
		if digit_sum_y < 10:
			return digit_sum_y
		print(digit_sum_y % 10 + recurse(digit_sum_y // 10))
		break 
string_num = '123'
iteration_k = 3
multiplier_z = string_num * iteration_k
digit_sum_y = sum(map(int,multiplier_z))

recurse(digit_sum_y)
