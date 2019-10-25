#hardworkers

def main():
    
    hours = int(input("Enter number of hours worked: "))
    rate = float(input("Enter hourly rate: "))
    
    if hours > 40:
        wage = (40 * rate) + (hours - 40) * rate * 1.5
    else:
        wage = hours * rate
    print("Your salary for this week is {}".format(wage))
    
main()
        