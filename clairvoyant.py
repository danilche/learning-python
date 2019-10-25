#clairvoyant.py
#converts input strings to numbers and add them up
import string
def main():
    
    uno, alpha = "x", string.ascii_lowercase
    alpha = uno + alpha
    due, beta = "x", string.ascii_uppercase
    beta = due + beta
    summa1 = 0
    summa2 = 0
    
    name = input("Enter your name: ")
    for x in range(len(name)):
        number1 = int(alpha.find(name[x]))
        if number1 < 0:
            number1 = 0
        summa1 = number1 + summa1

    for x in range(len(name)):
        number2 = int(beta.find(name[x]))
        if number2 < 0:
            number2 = 0
        summa2 = number2 + summa2
    
    print(summa1 + summa2)
       
main()