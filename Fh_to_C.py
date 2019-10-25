# Fh_to_C.py
# A program to convert Fahrenheit temperatures to Celsius


def main () :
    fahrenheit = float(input ("What is the Fahrenheit temperature? ") )
    celsius = (fahrenheit - 32) * 5 / 9
    print ("The temperature is", round(celsius, 2), "degrees Celsius.")
    
main ()