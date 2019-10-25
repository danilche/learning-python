import math

def ladder():
	height = float(input("Enter height of house: "))
	angle_deg = int(input("Enter ladder angle in degrees: "))
	angle_rad = math.pi / 180 * angle_deg
	length = height / math.sin(angle_rad)
	print()
	print()
	print("Length of a ladder has to be", round(length, 2))
	
ladder()
