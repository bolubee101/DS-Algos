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
		if digit_sum_y < 10 or digit_sum_y <= 30:
			return (digit_sum_y)
		a = digit_sum_y % 10 + recurse(digit_sum_y // 10)
		print(a)
		if a > 10:
			print(a % 10 + recurse(a // 10))
		else:
			print(a)
		break


string_num = input('')
iteration_k = int(input())
multiplier_z = string_num * iteration_k
print(multiplier_z)
digit_sum_y = sum(map(int,multiplier_z))
print(f' digit_sum is {digit_sum_y}')

recurse(digit_sum_y)
