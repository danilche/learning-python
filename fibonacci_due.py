def fibonacci():
    n = int(input("Enter number: "))
    a, b = 1, 1

    for j in range (n - 2):
        a = a + b
        b = a - b
        
    print("Number you asked for is", a)
    
fibonacci()