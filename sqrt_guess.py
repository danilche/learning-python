# This program guesses square root of a user defined number

import math

def square_root():
	x = int(input("Enter a number to extract square root from: "))
	num_guess = int(input("Enter how many times you want square root to be \
guessed: "))
	guess = x/2
	for i in range (num_guess):
		guess = (guess + x/guess) / 2

	print ()
	print("------------------")
	print("Your guess is", guess)
	print()
	print("Square root of", x, "is", math.sqrt(x))
	print()
	error = guess - math.sqrt(x)
	print("Your margin of error is", round(error, 8))
	
square_root()