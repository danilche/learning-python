#acronym

def main():
    
    phrase = input("Enter your phrase to be acronymized: ")
    for j in phrase.split():
        print (j[0].upper(), end="")
        
main()