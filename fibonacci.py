# This program prints Fibonacci sequence

def fibonacci():
	n = int(input("Enter an integer: "))
	a = 1
	s = 1
	for j in range (n - 2):
		s = a + s
		a = s - a
	print()
	print("--------------")
	print("Result is", s)

	input("<-------->")

fibonacci()