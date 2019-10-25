#syracuse

def main():
    x = int(input("Enter the starting value: "))
    cnt = 0
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            cnt += 1
        else:
            x = 3*x + 1
            cnt += 1
        print(int(x))
    print("Number of iterations needed is", cnt)
main()