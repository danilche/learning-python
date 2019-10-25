from random import *

def strengthHome(strength, homeIndex):
    strength_home_index = (strength + homeIndex) / 100
    return strength_home_index

def strengthAway(strength, awayIndex):
    strength_away_index = (strength - awayIndex) / 100
    return strength_away_index
 
def score(strength_index):
    score = 0
    for j in range(160):    
        if random() <= strength_index:
            score = score + 1
        else:
            pass
    return score

def overtime(strength_index):
    ot_score = 0
    for j in range(30):    
        if random() <= strength_index:
            ot_score = ot_score + 1
        else:
            pass
    return ot_score

def inputs():      
    name = input("Enter team name: ")
    strength = int(input("Enter team strength on scale 1 - 100: "))
    homeIndex = int(input("Enter home court index on scale 1 - 5: "))
    awayIndex = int(input("Enter away court index on scale 1 - 5: "))
    return name, strength, homeIndex, awayIndex

def game(team_a, team_b):    
    scoreA = score(strengthHome(team_a[1], team_a[2])) 
    scoreB = score(strengthAway(team_b[1], team_b[3]))
    if scoreA > scoreB:
        winner = team_a
    elif scoreA < scoreB:
        winner = team_b
    else:
        while scoreA == scoreA:
            otA = overtime(strengthHome(team_a[1], team_a[2]))
            otB = overtime(strengthAway(team_b[1], team_b[3]))
            scoreA = scoreA + otA
            scoreB = scoreB + otB
            if scoreA > scoreB:
                winner = team_a
            else:
                winner = team_b

    return scoreA, scoreB, winner

def main():    
    team_a = inputs()
    team_b = inputs()
    scoreA, scoreB, winner = game(team_a, team_b)
    print("{} - {}    {}:{}".format(team_a[0], team_b[0], scoreA, scoreB))
    print("Winner is", winner[0])
    
main()
