# this program calculates the volume and surface area of a sphere from its radius

import math


def sphere():

	r = eval(input("Enter the value of r: "))
	volume = 4 / 3 * math.pi * r * r * r
	surface = 4 * math.pi * r * r
	print()
	print("*********************")
	print("Volume is", round(volume, 3), "and surface is", round(surface, 3))

	input("Press <Enter> to exit")

sphere()