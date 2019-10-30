from random import *

def inputs():
          
    name = input("Enter team name: ")
    strength = int(input("Enter team strength on scale 30 - 50: "))
    return name, strength

def normal_set(strength_a, strength_b):
    score_a = 0
    score_b = 0
    serving = "A"
    while not ((score_a >= 25 or score_b >= 25) 
                and (abs(score_a - score_b) >= 2)):
        if serving == "A":
            if random() < strength_a / 100:
                score_a += 1
            else:
                serving = "B"
        else: 
            if random() < strength_b / 100:
                score_b += 1
            else:
                serving = "A"
    return score_a, score_b

def tie_break(strength_a, strength_b):
    score_a = 0
    score_b = 0
    serving = "A"
    while not ((score_a >= 15 or score_b >= 15) 
                and (abs(score_a - score_b) >= 2)):
        if serving == "A":
            if random() < strength_a / 100:
                score_a += 1
            else:
                serving = "B"
        else: 
            if random() < strength_b / 100:
                score_b += 1
            else:
                serving = "A"
    return score_a, score_b

def result(result_a, result_b, score_a, score_b):
    if score_a > score_b:
        result_a.append(1)
    else:
        result_b.append(1)
    return result_a, result_b

def match(name_a, strength_a, name_b, strength_b):
    result_a = []
    result_b = [] 
    first_set = normal_set(strength_a, strength_b)
    result(result_a, result_b, first_set[0], first_set[1])
    second_set = normal_set(strength_a, strength_b)
    result(result_a, result_b, second_set[0], second_set[1])
    third_set = normal_set(strength_a, strength_b)
    result(result_a, result_b, third_set[0], third_set[1])
    if sum(result_a) == 3 or sum(result_b) == 3:
        print("{} - {} {}:{}".format(name_a, name_b, sum(result_a),
              sum(result_b)))
        print("({}:{}, {}:{}, {}:{})".format
              (first_set[0], first_set[1],
              second_set[0], second_set[1], 
              third_set[0], third_set[1]))
    else:
        fourth_set = normal_set(strength_a, strength_b)
        result(result_a, result_b, fourth_set[0], fourth_set[1])
        if sum(result_a) == 3 or sum(result_b) == 3:
            print("{} - {} {}:{}".format(name_a, name_b, sum(result_a),
                  sum(result_b)))
            print("({}:{}, {}:{}, {}:{}, {}:{})".format
                  (first_set[0], first_set[1],
                   second_set[0], second_set[1],
                   third_set[0], third_set[1],
                   fourth_set[0], fourth_set[1]))
        else:
            fifth_set = tie_break(strength_a, strength_b)
            result(result_a, result_b, fifth_set[0], fifth_set[1])
            print("{} - {} {}:{}".format(name_a, name_b, sum(result_a),
                  sum(result_b)))
            print("({}:{}, {}:{}, {}:{}, {}:{}, {}:{})".format
                  (first_set[0], first_set[1],
                  second_set[0], second_set[1], 
                  third_set[0], third_set[1],
                  fourth_set[0], fourth_set[1], 
                  fifth_set[0], fifth_set[1]))
    if sum(result_a) == 3:
        winner, strength = name_a, strength_a
    else:
        winner, strength = name_b, strength_b
    return winner, strength

def isWinner(team_a, team_b, win, team_a_points, team_b_points):
#    team_a_points = 0
#    team_b_points = 0
    if win[0] == team_a:
        team_a_points += 2
    else:
        team_b_points += 2
    return team_a_points, team_b_points
    
def calcStandings(team_a, team_a_points, 
                  team_b, team_b_points,
                  team_c, team_c_points, 
                  team_d, team_d_points):
    pool_dict = {team_a:team_a_points, team_b:team_b_points,
            team_c:team_c_points, team_d:team_d_points}
    points = sorted(pool_dict.values(), reverse=True)
    teams = sorted(pool_dict, key=pool_dict.get, reverse=True)
    sep = "      "
    print()
    print("Standings:")
    print()
    for j in range(4):
        print("{}{}{}".format(teams[j], sep, points[j]))
    return pool_dict
            
def group(team_A, strength_A,
          team_B, strength_B,
          team_C, strength_C,
          team_D, strength_D):
    team_A_points = 0
    team_B_points = 0
    team_C_points = 0
    team_D_points = 0

#   This is round one   
    win_1 = match(team_A, strength_A, team_B, strength_B)
    team_A_points, team_B_points = isWinner(team_A, team_B, win_1,
                                            team_A_points, team_B_points)
    win_2 = match(team_C, strength_C, team_D, strength_D)
    team_C_points, team_D_points = isWinner(team_C, team_D, win_2,
                                            team_C_points, team_D_points)
    calcStandings(team_A, team_A_points, 
                  team_B, team_B_points, 
                  team_C, team_C_points, 
                  team_D, team_D_points)
    
#   This is round two
    print("-----------------------------")
    win_3 = match(team_B, strength_B, team_D, strength_D)
    team_B_points, team_D_points = isWinner(team_B, team_D, win_3,
                                            team_B_points, team_D_points)
    win_4 = match(team_C, strength_C, team_A, strength_A)
    team_C_points, team_A_points = isWinner(team_C, team_A, win_4,
                                            team_C_points, team_A_points)
    calcStandings(team_A, team_A_points, 
                  team_B, team_B_points, 
                  team_C, team_C_points, 
                  team_D, team_D_points)
    
#   This is round three
    print("-----------------------------")
    win_5 = match(team_D, strength_D, team_A, strength_A)
    team_D_points, team_A_points = isWinner(team_D, team_A, win_5,
                                            team_D_points, team_A_points)
    win_6 = match(team_B, strength_B, team_C, strength_C)
    team_B_points, team_C_points = isWinner(team_B, team_C, win_6,
                                            team_B_points, team_C_points)
    finalStandings = calcStandings(team_A, team_A_points, 
                  team_B, team_B_points, 
                  team_C, team_C_points, 
                  team_D, team_D_points)
    ordFinalStandings = (sorted(finalStandings, key=finalStandings.get, 
                                reverse=True))
    quarter1, quarter2 = ordFinalStandings[0], ordFinalStandings[1]
    return quarter1, quarter2
    
    
def mainTournament():
    team_1, strength_1 = inputs()
    team_2, strength_2 = inputs()
    team_3, strength_3 = inputs()
    team_4, strength_4 = inputs()
    team_5, strength_5 = inputs()
    team_6, strength_6 = inputs()
    team_7, strength_7 = inputs()
    team_8, strength_8 = inputs()
    groupA = group(team_1, strength_1,
                   team_2, strength_2,
                   team_3, strength_3,
                   team_4, strength_4)
    groupB = group(team_5, strength_5,
                   team_6, strength_6,
                   team_7, strength_7,
                   team_8, strength_8)
    return groupA, groupB

def playOff(team_A, team_B,
            team_C, team_D):
    finalist_1 = 