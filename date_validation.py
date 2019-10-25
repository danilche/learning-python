#date validation
                
def main():
    
    date = input("Enter date in DD/MM/YYYY format: ")
    date = date.split("/")
    month, day, year = int(date[0]), int(date[1]), int(date[2])
    
    if month in (1, 3, 5, 7, 8, 10, 12):
        if 0 <= year <= 9999: 
            if day in range(1, 32):
                print("This is a valid date")
            else:
                print("This is not a valid date")
        else:
            print("This is not a valid date")
    elif month in (4, 6, 9, 11):
        if 0 <= year <= 9999: 
            if day in range(1, 31):
                print("This is a valid date")
            else:
                print("This is not a valid date")
        else:
            print("This is not a valid date")
    elif month == 2:
        if 0 <= year <= 9999:
            if year % 4 == 0:
                if year in list(range(100, year + 1, 100)):
                    if year % 400 ==0:
                        if day in range(1, 30):
                            print("This is a valid date")
                        else:
                            print("This is not a valid date")
                    else:
                        print("This is not a valid date")
                else:
                    print("This is not a valid date")
            else:
                if day in range(1, 29):
                    print("This is a valid date")
                else:
                    print("This is not a valid date")
        else:
            print("This is not a valid date")
    else:
        print("This is not a valid date")
                 
main()
        