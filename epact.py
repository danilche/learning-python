
import math

def easter():
	year = int(input("Enter A.D.: "))
	c = year // 100
	epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
	print()
	print("----------------------")
	print("Epact is", epact)
	print()
	print()
	print()
	input("Press <E> to quit")

easter()