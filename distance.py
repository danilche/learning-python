
import math

def distance():
	x1, y1 = eval(input("Enter coordinates separated by comma: "))
	x2, y2 = eval(input("Enter coordinates separated by comma: "))
	distance = math.sqrt((y2 - y1) + (x2 - x1))
	print()
	print("----------------------")
	print("Distance is", round(distance, 3))
	print()
	print()
	print()
	input("Press <E> to quit")
distance()