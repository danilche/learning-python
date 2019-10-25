def squareEach(nums):
    for j in range(len(nums)):
        nums[j] = int(nums[j])*int(nums[j]) 
    return nums


def main():
    x = input("Enter numbers separated by comma: ")
    x = x.split(",")
    print(squareEach(x))

main()