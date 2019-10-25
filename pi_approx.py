# This program sums sequence of numbers and prints approximation of pi

import math

def weird():
	n = int(input("Enter a number: "))
	sum = 4
	sum1 = -4 / 3
	for cnt in range(5, n + 1, 4):
		sum = sum + 4 / cnt
		print()
		print(sum)

	for cnt1 in range(7, n + 1, 4):
		sum1 = sum1 - 4 / cnt1
		print()
		print(sum1)
	final = sum + sum1
	pi_app = (4 * math.atan(1 / 5) - math.atan(1 / 239)) *4
	print()
	print("Final result is", final)
	print()
	print("Approx of pi is", pi_app)

	input("<>")

weird()