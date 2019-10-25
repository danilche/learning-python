#Caesar cipher with string shift
def main():
    
    alpha = " abcdefghijklmnopqrstuvwxyz"
    name = input("Enter your text here: ")
    key = int(input("Enter your key: "))
    a1, a2 = alpha[:key], alpha[key:len(alpha)]
    alpha1 = a2 + a1
    my_list = []
    for x in range(len(name)):
        my_list.append(int(alpha1.find(name[x])))
    
    print(my_list)
    print("******************************")
    
    rijec=""
    for x in my_list:
        rijec = rijec + alpha1[x - key]
    
    print(rijec, end="")
    print("\n")
    print("------------------------------")
    
    my_list1 = []
    for x in range(len(rijec)):
        my_list1.append(int(alpha1.find(rijec[x])))
    
    print(my_list1)
    print("#############################")
 
    
          
    nova_rijec=""
    for x in my_list1:
        nova_rijec = nova_rijec + alpha1[x + key]
    
    print(nova_rijec, end="")
    print("\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
       
main()