#word count batch

def main():
    
    with open('/home/dane/Documents/wrangling/puss_in_boots.txt') as path:
        my_file = path.read()
    my_list = []
    
    for j in my_file:
        my_list = my_file.split()
    lgt = len(my_list)
    print("Your file has {} words".format(lgt))
    
    
main()