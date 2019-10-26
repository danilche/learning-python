#this is work in progress

from random import *

def strengthHome(strength, homeIndex, currentForm):
    strength_home_index = (strength + homeIndex + currentForm) / 100
    return strength_home_index

def strengthAway(strength, awayIndex, currentForm):
    strength_away_index = (strength - awayIndex + currentForm) / 100
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
    strength = int(input("Enter team strength on a scale 30 - 50: "))
    homeIndex = int(input("Enter home court index on a scale 0 - 3: "))
    awayIndex = int(input("Enter away court index on a scale 0 - 3: "))
    currentForm = int(input("Enter form index on a scale from -5 to 5: "))
    return name, strength, homeIndex, awayIndex, currentForm

def game(team_a, team_b):    
    scoreA = score(strengthHome(team_a[1], team_a[2], team_a[4])) 
    scoreB = score(strengthAway(team_b[1], team_b[3], team_b[4]))
    if scoreA > scoreB:
        winner = team_a
    elif scoreA < scoreB:
        winner = team_b
    else:
        while scoreA == scoreA:
            otA = overtime(strengthHome(team_a[1], team_a[2], team_a[4]))
            otB = overtime(strengthAway(team_b[1], team_b[3], team_b[4]))
            scoreA = scoreA + otA
            scoreB = scoreB + otB
            if scoreA > scoreB:
                winner = team_a
            else:
                winner = team_b

    return scoreA, scoreB, winner

def main():    
    team_1 = inputs()
    team_2 = inputs()
    team_3 = inputs()
    team_4 = inputs()
    team_1_wins = 0
    team_2_wins = 0
    team_3_wins = 0
    team_4_wins = 0
    team_1_loses = 0
    team_2_loses = 0
    team_3_loses = 0
    team_4_loses = 0
    print("---------------------------")
    scoreA, scoreB, winner = game(team_1, team_2)
    if winner == team_1:
        team_1_wins, team_2_loses = team_1_wins + 1, team_2_loses + 1
    else:
        team_2_wins, team_1_loses = team_2_wins + 1, team_1_loses + 1
    print("{} - {}    {}:{}".format(team_1[0], team_2[0], scoreA, scoreB))
    print("---------------------------")
    print("Standings")
    print("{}     {} - {}".format(team_a[0], team_a_wins, team_a_loses))
    print("{}     {} - {}".format(team_b[0], team_b_wins, team_b_loses))
    print("---------------------------")
    scoreA, scoreB, winner = game(team_3, team_4)
    if winner == team_a:
        team_a_wins, team_b_loses = team_a_wins + 1, team_b_loses + 1
    else:
        team_b_wins, team_a_loses = team_b_wins + 1, team_a_loses + 1
    print("{} - {}    {}:{}".format(team_b[0], team_a[0], scoreB, scoreA))
    print("-------------------------------------")
    print("Standings")
    print("{}     {} - {}".format(team_a[0], team_a_wins, team_a_loses))
    print("{}     {} - {}".format(team_b[0], team_b_wins, team_b_loses))
    
main()
