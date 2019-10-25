# this program determines the distance to a lightning strike based on
# the time elapsed between the flash and the sound of thunder


def lightning_strikes_twice():

	t = int(input("Enter number of seconds passed since the lightning: "))
	sos = 1100
	distance_in_feet = t * sos
	distance_in_miles = round(distance_in_feet / 5280, 2)
	print()
	print("--------------------")
	print("Distance is", distance_in_feet, "feet")
	print("--------------------")
	print("Distance is", distance_in_miles, "miles")
	if distance_in_miles < 1:
		print()
		print("!!!!!!!!!!!!!!!!!!")
		print()
		print("Oh boy, it hit ya, didn't it?!")
		print()
		print("R.I.P")
		print()
		print("!!!!!!!!!!!!!!!!!!")
	else:
		print()
		print("----------------------------------")
		print("You're one lucky bastud, ya know!")
	print()
	print()
	print()
	print()
	input("Press <Enter> to exit")

lightning_strikes_twice()