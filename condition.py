def strange():
    n = int(input("Enter an integer between 1 and 100: "))
    if n < 1 or n > 100:
        print("You're cheating!")
    elif n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range (2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range (6, 21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
strange()