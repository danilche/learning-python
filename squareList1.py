def squareEach(nums):
    sq = []
    for j in nums:
        q = int(j)*int(j)
        sq.append(q) 
    return sq


def main():
    x = input("Enter numbers separated by comma: ")
    x = x.split(",")
    print(squareEach(x))

main()