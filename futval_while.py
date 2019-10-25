# futval.py
# A program to compute the value of an investment

def main ():
    init_principal = float(input("Enter the initial principal: "))
    principal = init_principal
    apr = float(input ("Enter the annual interest rate: "))
    cnt = 0
    print("\n" * 2)
    print("Year    Value")
    print("--------------")
    while principal <= init_principal * 2:
        principal = principal * (1 + apr)
        cnt += 1
        print ("{}    {:.2f}".format(cnt, principal).center(16))
    print("---------------")
    print("Number of years needed to double your initial investment is", cnt)

main ()