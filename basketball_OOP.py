#this is work in progress

from random import *

class Team:

    def __init__(self, name, strength, wins, loses):
        self.name = name
        self.strength = float(strength)
        self.wins = int(wins)
        self.loses = int(loses)

    def getName(self):
        return self.name

    def getStrength(self):
        return self.strength

    def getWins(self):
        return self.wins
    
    def updateWins(self):
        self.wins = self.wins + 1

    def loses(self):
        return self.loses
    
    def updateLoses(self):
        self.loses = self.loses + 1

def team_inputs():
    name = input("Enter name: ")
    strength = int(input("Enter strength: "))
    wins, loses = 0, 0
    return name, strength, wins, loses

def make_team(someInput):
    name, strength, wins, loses = someInput
    return Team(name, strength, wins, loses)
 
def score_loop(strength, number_of_loops):
    score = 0
    for j in range(number_of_loops):    
        if random() <= strength/ 100:
            score = score + 1
        else:
            pass
    return score

def game(team_a, team_a_strength,
         team_b, team_b_strength):    
    score_a = score_loop(team_a_strength, 160) 
    score_b = score_loop(team_b_strength, 160)
    while score_a == score_b:
        ot_a = score_loop(team_a_strength, 30)
        ot_b = score_loop(team_b_strength, 30)
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

def updates_wins_and_loses(team_a, team_b, winner):
    if winner == team_a.name:
        team_a.updateWins(), team_b.updateLoses()
    else:
        team_b.updateWins(), team_a.updateLoses()
        

def print_score(team_a_name, team_b_name, score_a, score_b):
    print("{} - {}    {}:{}".format(team_a_name, team_b_name, score_a, score_b))

    
# def print_standings(team_a, team_b, team_c, team_d,
#                     team_a_wins, team_b_wins, team_c_wins, team_d_wins,
#                     team_a_loses, team_b_loses, team_c_loses, team_d_loses):
#     print("{}     {} - {}".format(team_a, team_a_wins, team_a_loses))
#     print("{}     {} - {}".format(team_b, team_b_wins, team_b_loses))
#     print("{}     {} - {}".format(team_c, team_c_wins, team_c_loses))
#     print("{}     {} - {}".format(team_d, team_d_wins, team_d_loses))

def print_standings(team_a, team_a_wins, team_a_loses,
                    team_b, team_b_wins, team_b_loses,
                    team_c, team_c_wins, team_c_loses, 
                    team_d, team_d_wins, team_d_loses):
    pool_wins = {team_a:team_a_wins, team_b:team_b_wins,
                 team_c:team_c_wins, team_d:team_d_wins}
    pool_loses = {team_a:team_a_loses, team_b:team_b_loses,
                 team_c:team_c_loses, team_d:team_d_loses}
    wins = sorted(pool_wins.values(), reverse=True)
    loses = sorted(pool_loses.values())
    teams = sorted(pool_wins, key=pool_wins.get, reverse=True)
    sep = "      "
    print()
    print("Standings:")
    print()
    for j in range(4):
        print("{}{}{}-{}".format(teams[j], sep, wins[j], loses[j]))

def round(team_a, team_b, team_c, team_d,):    
    team_a_score, team_b_score = game(team_a.name, team_a.strength,
                                          team_b.name, team_b.strength)
    updates_wins_and_loses(team_a, team_b, winner_is(team_a.name, team_b.name,
                                                     team_a_score, team_b_score))
    team_c_score, team_d_score = game(team_c.name, team_c.strength,
                                      team_d.name, team_d.strength)
    updates_wins_and_loses(team_c, team_d, winner_is(team_c.name, team_d.name,
                                                     team_c_score, team_d_score))
    print("---------------------------")
    print_score(team_a.name, team_b.name,
               team_a_score, team_b_score)
    print_score(team_c.name, team_d.name,
               team_c_score, team_d_score)
    print()
    print_standings(team_a.name, team_a.wins, team_a.loses,
                    team_b.name, team_b.wins, team_b.loses,
                    team_c.name, team_c.wins, team_c.loses,
                    team_d.name, team_d.wins, team_d.loses)
    print("---------------------------")

def main():
        
    team_1 = make_team(team_inputs())
    team_2 = make_team(team_inputs())
    team_3 = make_team(team_inputs())
    team_4 = make_team(team_inputs())
    
    ###--1st round
    ###-----------------------------------
    round_1 = round(team_1, team_2, team_3, team_4)
    ###-----------------------------------
    ###--2nd round
    ###-----------------------------------
    round_2 = round(team_3, team_2, team_4, team_1)
    ###-----------------------------------
    ###--3rd round
    ###-----------------------------------
    round_3 = round(team_1, team_3, team_2, team_4)
    ###--4th round
    ###-----------------------------------
    round_1 = round(team_4, team_3, team_2, team_1)
    ###-----------------------------------
    ###--5th round
    ###-----------------------------------
    round_2 = round(team_1, team_4, team_2, team_3)
    ###-----------------------------------
    ###--6th round
    ###-----------------------------------
    round_3 = round(team_4, team_2, team_3, team_1)
    

    
if __name__ == '__main__':
    main()
