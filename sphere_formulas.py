import math

def sphereArea(r):
    A = 4 * math.pi * r*r
    return round(A, 2)

def sphereVolume(r):
    V = 4/3 * math.pi * r*r*r
    return round(V, 2)
    
def main():
    r = float(input("Enter sphere radius: "))
    print()
    print(sphereArea(r))
    print()
    print(sphereVolume(r))
    
main()