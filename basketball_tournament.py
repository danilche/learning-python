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
    return name, strength

def game(x, y):    
    
    score_x = score(prob(x, y)) 
    score_y = score(prob(y, x))
    if score_x > score_y:
        winner = x
    elif score_x < score_y:
        winner = y
    else:
        while score_x == score_y:
            ot_x = overtime(prob(x, y))
            ot_y = overtime(prob(y, x))
            score_x = score_x + ot_x
            score_y = score_y + ot_y
            if score_x > score_y:
                winner = x
            else:
                winner = y

    return score_x, score_y, winner

#def series():
#    game_1 = game(x, y)
#    game_2 = game(y, x)
    
def main():
    a = inputs()
    b = inputs()
#    c = inputs()
#    d = inputs()
    winner1 = game(a, b)
    print("The winner is", winner)
    print("The score was {} - {} {}:{}".format(a[0], b[0], score_x, score_y))
#    winner2 = game(b, a)
#    final = game(winner1, winner2)
    
    
main()