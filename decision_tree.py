def main():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    d = int(input("Enter 4th number: "))
    
    if a >= b:
        if a >= c:
            if a >= d:
                print("Greatest is", a)
            else:
                print("Greatest is", d)
        elif c >= d:
            print("Greatest is", c)
        else:
            print("Greatest is", d)
    else:
        if b >= c:
            if b >= d:
                print("Greatest is", b)
            else:
                print("Greatest is", d)
        elif c >= d:
            print("Greatest is", c)
        else:
            print("Greatest is", d)
            
main()