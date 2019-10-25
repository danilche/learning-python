#improved chaos

def main():
    user_input = input("Enter two numbers between 0 and 1, separated by a comma: ")
    r = int(input("Enter number of iterations: "))
    my_list = user_input.split(",")
    x, y = float(my_list[0]), float(my_list[1])
    sep1 = "    "
    sep2 = "  "
    print("index {0}{1}{3}{3}{2}".format(sep2, x, y, sep1))
    print("---------------------------")
    for j in range(r):
        x = 3.9 * x *(1 - x)
        y = 3.9 * y *(1 - y)
        print(("{1}{0}{2:6f}{0}{3:6f}".format(sep1, j, x, y)).center(30))
    
main()