
numbers = []
cubes = []

def numSum(n):
    for j in range (n):
        numbers.append(j+1)
    return sum(numbers)

def cubSum(j):
    for j in numbers:
        cubes.append(j*j*j)
    return sum(cubes)


def main():
    n = int(input("Enter final number (n): "))
    print()
    print(numSum(n))
    print()
    print(cubSum(n))
    
main()