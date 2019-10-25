def fibonacci(n):
    a, b, fi = 0, 1, [1]
    
    for j in range (n):
        a = a + b
        fi.append(a)
        b = b + a
        fi.append(b)
    return fi[n-1]
        
        
def main():
    
    numero = int(input("Enter n-th number you'd like displayed: "))
    print("Your number is", fibonacci(numero))
    
main()

    
