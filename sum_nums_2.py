def sumList(nums): 
    a = 0
    for j in range(len(nums)):
        a = a + nums[j]    
    return a


def main():
    x = input("Enter numbers separated by comma: ")
    x = x.split(",")
    y = []
    for j in range(len(x)):
        y.append(int(x[j]))
    print(sumList(y))

main()