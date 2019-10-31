#this is a version of basketball simulation

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

def overtime(prob):
    ot_score = 0
    for j in range(30):    
        if random() <= prob:
            ot_score = ot_score + 1
        else:
            pass
    return ot_score

def inputs():
          
    name = input("Enter team name: ")
    strength = int(input("Enter team strength on scale 1 - 100: "))
    home = int(input("Enter home court index on scale 1 - 5: "))
    away = int(input("Enter away court index on scale 1 - 5: "))
    return name, strength, home, away

def game(a, b):    
    
    score1 = score(prob(a[1] + a[2], b[1] - b[3])) 
    score2 = score(prob(b[1] - b[3], a[1] + a[2]))
    score3 = score(prob(a[1] - a[3], b[1] + b[2]))
    score4 = score(prob(b[1] + b[2], a[1] - a[3]))
    
    print("{} - {}    {}:{}".format(a[0], b[0], score1, score2))
    print("{} - {}    {}:{}".format(b[0], a[0], score4, score3))
    print("Total result is {} - {} {}:{}".format(a[0], b[0], score1+score3, score2+score4))
    print()
    if score1+score3 > score2+score4:
        winner = a
        print("The winner is {}".format(winner[0]))
        print()
    elif score1+score3 < score2+score4:
        winner = b
        print("The winner is {}".format(winner[0]))
        print()
    else:
        print("This game is tied, we'll need an overtime!")
        while score1+score3 == score2+score4:
            ot_1 = overtime(prob(a[1] - a[3], b[1] + b[2]))
            ot_2 = overtime(prob(b[1] + b[2], a[1] - a[3]))
            score3 = score3 + ot_1
            score4 = score3 + ot_2
            print("Final result of Game 2 is {} - {} {}:{}".format(b[0], a[0], score4, score3))
            print("Total result is now {} - {} {}:{}".format(a[0], b[0], score1+score3, score2+score4))
            print()
            if score1+score3 > score2+score4:
                winner = a
                print("After OT, winner is", winner[0])
            elif score1+score3 < score2+score4:
                winner = b
                print("After OT, winner is", winner[0])

    return winner


def main():
    a = inputs()
    b = inputs()
    winner1 = game(a, b)
    a = inputs()
    b = inputs()
    winner2 = game(a, b)
    final = game(winner1, winner2)
    print()
    print("Tournament winner is {}".format(final[0]))
    
main()