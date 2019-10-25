# futval.py
# A program to compute the value of an investment

def main ():
    principal = float(input("Enter the initial principal: "))
    apr = float(input ("Enter the annual interest rate: "))
    year = int(input("Enter number of years: "))
    sep = "    "
    print("\n" * 2)
    print("Year{}Value".format(sep))
    print("--------------")
    for i in range(1, year + 1):
        principal = principal * (1 + apr)
        print ("{}{}{:.2f}".format(i, sep, principal).center(16))

main ()