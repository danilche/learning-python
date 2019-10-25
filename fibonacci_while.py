#fibonacci

def main():
    n = int(input("Enter a whole number: "))
    counter = 1
    a = 1
    b = 1
    fib = [1, 1]
    while counter <= n:
        b = b + a
        a = b - a
        counter += 1
        fib.append(b)
    print(fib[n])
main()
        