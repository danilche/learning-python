#students

def main():
    
    credit = int(input("Enter number of credits: "))
    
    if credit < 7:
        print("You're a Freshman")
    elif 7 <= credit < 16:
        print("You're a Sophomore")
    elif 16 <= credit < 26:
        print("You're a Junior")
    else:
        print("You're a Senior")
    
main()
        