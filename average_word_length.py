#average word length

def main():
    
    sentence = input("Enter your sentence here: ")
    print(sentence)
    s1 = sentence.replace(",", "")
    print(s1)
    s2 = s1.replace(".", "")
    print(s2)
    
    my_list = s2.split()
    
    num_list = []
    for x in range(len(my_list)):
        num_list.append(len(my_list[x]))
   
    average_len = sum(num_list) / len(num_list)
    print("{} is the average word length in you sentence".format(round(average_len, 2)))
    
main()