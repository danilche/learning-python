import math

def matematica():

	a =  float(input("Enter coeff a: "))
	b =  float(input("Enter coeff b: "))
	c =  float(input("Enter coeff c: "))

	discRoot = math.sqrt(b * b - 4 * a * c)
	root1 = (-b + discRoot) / (2 * a)
	root2 = (-b - discRoot) / (2 * a)

	print()
	print("The solutions are:", root1, root2)

matematica()
