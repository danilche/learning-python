def fibonacci():
    n = int(input("Enter number: "))
    a, b, fi = 0, 1, [1]
    
    for j in range (n):
        a = a + b
        fi.append(a)
        b = b + a
        fi.append(b)
    
    print("Number you asked for is", fi[n - 1])
    
fibonacci()