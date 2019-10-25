#leap years
    
def main():

    year = int(input("Enter year: "))
    
    if year % 4 == 0:
        if year in list(range(100, year + 1, 100)):
            if year % 400 ==0:
                print("This is leap year")
            else:
                print("This ain't no leap year!")
        else:
            print("This is leap year")
    else:
        print("This ain't no leap year!")
                 
main()
        