#word count

def main():
    
    sentence = input("Enter your sentence here: ")
    
    my_list = sentence.split()
    
    print("Your sentence has {} words".format(len(my_list)))
    
main()