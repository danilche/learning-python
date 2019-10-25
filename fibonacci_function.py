
def fibonacci(n):
    a, b = 1, 1

    for j in range (n - 2):
        a = a + b 
        b = a - b
    return a
        
        
def main():
    
    numero = int(input("Enter n-th number you'd like displayed: "))
    print("Your number is", fibonacci(numero))
    
main()
    