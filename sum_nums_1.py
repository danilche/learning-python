def sumList(nums): 
    return sum(nums)


def main():
    x = input("Enter numbers separated by comma: ")
    x = x.split(",")
    y = []
    for j in range(len(x)):
        y.append(int(x[j]))
    print(sumList(y))

main()