# this program prints the sum of all natural numbers up to the one defined by user

def summa():
	n = int(input("Enter a natural number: "))
	c = 1
	print()
	for n in range(2, n + 1):
		c = c + n
	print()
	print("Sum of all numbers up to n is", c)
	input("----------------------------------")
summa()
