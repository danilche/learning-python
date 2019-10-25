def main():
    
    entry = input("Enter your text here: ")
    key = int(input("Enter your key: "))
    new_entry = ""
    for j in entry:
        x = ord(j)
        coded = x + key
        print(coded)
        new_entry = new_entry + chr(coded)
    
    print(new_entry)
    print(type(new_entry))
    
    new = ""
    for j in new_entry:
        x = ord(j)
        coded = x - key
        new = new + chr(coded)
        
    print(new)
       
main()