# this program prints the sum of numbers defined by user

def average():
	lops = int(input("Enter how many numbers to be summed: "))
	sum = 0
	print()
	for n in range(lops):
		n = int(input("Enter a number: "))
		sum = sum + n
	average = sum / lops
	print()
	print("---------------------")
	print("The average is", float(average))
	input("---------------------")
average()