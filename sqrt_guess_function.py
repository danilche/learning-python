import math

def square_root(number, times):
    guess = number/2
    for i in range (times):
        guess = (guess + number / guess) / 2
    return guess


def main():
    x = int(input("Enter a number to extract square root from: "))
    num_guess = int(input("Enter how many times you want square root to be \
guessed: "))
    print ()
    print("------------------")
    print("Your guess is", square_root(x, num_guess))
    print()
    print("Square root of", x, "is", math.sqrt(x))
    print()
    error = square_root(x, num_guess) - math.sqrt(x)
    print("Your margin of error is", round(error, 8))
	
main()
