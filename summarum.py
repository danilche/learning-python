# this program prints the sum of numbers defined by user

def summarum():
	lops = int(input("Enter how many numbers to be summed: "))
	sum = 0
	print()
	for n in range(lops):
		n = int(input("Enter a number: "))
		sum = sum + n
	print()
	print("---------------------")
	print(sum)
	input("---------------------")
summarum()