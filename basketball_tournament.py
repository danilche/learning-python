#this is work in progress

from random import *

def input_name():      
    name = input("Enter team name: ")
    return name

def input_strength():
    strength_index = int(input("Enter team strength on a scale 30 - 50: "))
    current_form = int(input("Enter form index on a scale from -5 to 5: "))
    strength = (strength_index + current_form) / 100
    return strength
 
def score_loop(strength, minutes):
    score = 0
    for j in range(minutes):    
        if random() <= strength:
            score = score + 1
        else:
            pass
    return score

def game(team_a, team_a_strength,
         team_b, team_b_strength):    
    score_a = score_loop(team_a_strength, 160) 
    score_b = score_loop(team_b_strength, 160)
    if score_a > score_b:
        pass
    elif score_a < score_b:
        pass
    else:
        while score_a == score_b:
            ot_a = score_loop(strength, 30)
            ot_b = score_loop(strength, 30)
            score_a = score_a + ot_a
            score_b = score_b + ot_b
    return score_a, score_b

def winner_is(team_a, team_b,
              score_a, score_b):
    if score_a > score_b:
        winner = team_a
    else:
        winner = team_b
    return winner

# def wins_loses_count(team_a, team_b, winner):
#     if winner == team_a:
#         team_a_wins, team_b_loses = team_a_wins + 1, team_b_loses + 1
#     else:
#         team_b_wins, team_a_loses = team_b_wins + 1, team_a_loses + 1
#     return team_a_wins, team_a_loses, team_b_wins, team_b_loses
        
def printScore(team_a_name, team_b_name, score_a, score_b):
    print("{} - {}    {}:{}".format(team_a_name, team_b_name, score_a, score_b))
    print("---------------------------")

def main():    
    team_1 = input_name()
    team_1_strength = input_strength()
    team_2 = input_name()
    team_2_strength = input_strength()
    team_1_score, team_2_score = game(team_1, team_1_strength, team_2, team_2_strength)
    print("{} - {}    {}:{}".format(team_1, team_2, team_1_score, team_2_score))
    
    

    

    
main()
