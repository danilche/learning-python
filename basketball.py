from random import *

def prob(x, y):
    prob = (x / (x + y))
    return prob
 
def score(prob):
    score = 0
    for j in range(160):    
        if random() <= prob:
            score = score + 1
        else:
            pass
    return score

def inputs():
          
    name = input("Enter team name: ")
    strength = int(input("Enter team strength on scale 1 - 100: "))
    home = int(input("Enter home court index on scale 1 - 5: "))
    away = int(input("Enter away court index on scale 1 - 5: "))
    return name, strength, home, away

def main():    
    a = inputs()
    b = inputs()

    for j in range (5):
        score1 = score(prob(a[1] + a[2], b[1] - b[3])) 
        score2 = score(prob(b[1] - b[3], a[1] + a[2]))
        score3 = score(prob(a[1] - a[3], b[1] + b[2]))
        score4 = score(prob(b[1] + b[2], a[1] - a[3]))
    
        print("{} - {}    {}:{}".format(a[0], b[0], score1, score2))
        print("{} - {}    {}:{}".format(b[0], a[0], score4, score3))


main()
