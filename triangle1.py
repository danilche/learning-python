
import math

def triangle():
	a = int(input("Enter a side: "))
	b = int(input("Enter b side: "))
	c = int(input("Enter c side: "))

	s = (a + b + c) / 2
	area = math.sqrt(s * (s - a) * (s - b) * (s - c))
	print()
	print()
	print("Area of the triangle is", round(area, 3))
	print()
	input("Press <> to exit")

triangle()