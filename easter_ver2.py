#easter ver 2.0
    
def main():
    
    year = int(input("Enter A.D. between 1900 and 2099: "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    easter = 22 + d + e
    e_but = 22 + d + e - 7
    
    if year not in range(1900, 2100):
        print("Not valid year")
    elif year in(1954, 1981, 2049, 2076):
        if e_but <=31:
            print("The date of Easter for A.D. {} is March {}".
                  format(year, e_but))
        else:
            print("The date of Easter for A.D. {} is April {}".
                  format(year, e_but - 31))      
    else:
        if easter <= 31:
            print("The date of Easter for A.D. {} is March {}".
                 format(year, easter))
        else:
            print("The date of Easter for A.D. {} is April {}".
                  format(year, easter - 31))
    
main()
        