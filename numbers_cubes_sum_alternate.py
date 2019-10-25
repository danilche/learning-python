
def numSum(n):
    x = 1
    for j in range(2, n+1):
        x = j + x
    return x

def cubSum(n):        
    x = 1
    for j in range(2, n+1):
        x = j*j*j + x
    return x

def main():
    n = int(input("Enter final number (n): "))
    print()
    print(numSum(n))
    print()
    print(cubSum(n))
    
main()
    