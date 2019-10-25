

def plane():
	x1, y1 = eval(input("Enter coordinates separated by comma: "))
	x2, y2 = eval(input("Enter coordinates separated by comma: "))
	slope = (y2 - y1) / (x2 - x1)
	print()
	print("----------------------")
	print("Slope is", slope)
	print()
	print()
	print()
	input("Press<E> to quit")
plane()