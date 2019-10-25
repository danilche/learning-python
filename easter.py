#easter
    
def main():
    
    year = int(input("Enter A.D. between 1982 and 2048: "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    easter = 22 + d + e
    
    if year not in range(1982, 2049):
        print("Not valid year")
    else:
        if easter <= 31:
            print("The date of Easter for A.D. {} is March {}".
                  format(year, easter))
        else:
            print("The date of Easter for A.D. {} is April {}".
                  format(year, easter - 31))
    
main()
        