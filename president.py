#eligible for president
    
def main():

    age = int(input("Enter age: "))
    citizenship = int(input("Enter number of years being a US citizen: "))
    
    if age < 18:
        print("You're minor! What were you thinking!")
    elif 18 < age < 25:
        print("You are an adult but not eligible for US Senate")
    elif 18 < age >= 25 and age < 30:
        if citizenship < 7:
            print("Your age fits but you haven't enough citizenship years to \
                  be eligible for US Senate")
        else:
            print("You are eligible for US Senate but not to be a presidential\
                  candidate")
    elif 18 < age >= 30:
        if citizenship < 9:
            print("Your age is sufficient but you haven't been a US citizen \
                  long enough to run for president campaign. Please try some \
                  other time")
        else:
            print("You are eligible to run for US presidency! Congrats!")
    
main()
        