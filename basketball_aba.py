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

# def team_inputs():
#     name = input("Enter name: ")
#     strength = int(input("Enter strength: "))
#     wins, loses = 0, 0
#     return name, strength, wins, loses
# 
# def make_team(someInput):
#     name, strength, wins, loses = someInput
#     return Team(name, strength, wins, loses)
 
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
   
def print_standings(team_a, team_a_wins, team_a_loses,
                    team_b, team_b_wins, team_b_loses,
                    team_c, team_c_wins, team_c_loses, 
                    team_d, team_d_wins, team_d_loses,
                    team_e, team_e_wins, team_e_loses,
                    team_f, team_f_wins, team_f_loses,
                    team_g, team_g_wins, team_g_loses,
                    team_h, team_h_wins, team_h_loses,
                    team_i, team_i_wins, team_i_loses,
                    team_j, team_j_wins, team_j_loses,
                    team_k, team_k_wins, team_k_loses,
                    team_l, team_l_wins, team_l_loses):
    pool_wins = {team_a:team_a_wins, team_b:team_b_wins,
                 team_c:team_c_wins, team_d:team_d_wins,
                 team_e:team_e_wins, team_f:team_f_wins,
                 team_g:team_g_wins, team_h:team_h_wins,
                 team_i:team_i_wins, team_j:team_j_wins,
                 team_k:team_k_wins, team_l:team_l_wins}
    pool_loses = {team_a:team_a_loses, team_b:team_b_loses,
                 team_c:team_c_loses, team_d:team_d_loses,
                 team_e:team_e_loses, team_f:team_f_loses,
                 team_g:team_g_loses, team_h:team_h_loses,
                 team_i:team_i_loses, team_j:team_j_loses,
                 team_k:team_k_loses, team_l:team_l_loses}
    wins = sorted(pool_wins.values(), reverse=True)
    loses = sorted(pool_loses.values())
    teams = sorted(pool_wins, key=pool_wins.get, reverse=True)
    sep = "      "
    print()
    print("Standings:")
    print()
    for j in range(12):
        print("{}{}{}-{}".format(teams[j], sep, wins[j], loses[j]))

def round(team_a, team_b, team_c, team_d, team_e, team_f,
          team_g, team_h, team_i, team_j, team_k, team_l):    
    team_a_score, team_b_score = game(team_a.name, team_a.strength,
                                          team_b.name, team_b.strength)
    updates_wins_and_loses(team_a, team_b, winner_is(team_a.name, team_b.name,
                                                     team_a_score, team_b_score))
    team_c_score, team_d_score = game(team_c.name, team_c.strength,
                                      team_d.name, team_d.strength)
    updates_wins_and_loses(team_c, team_d, winner_is(team_c.name, team_d.name,
                                                     team_c_score, team_d_score))
    team_e_score, team_f_score = game(team_e.name, team_e.strength,
                                      team_f.name, team_f.strength)
    updates_wins_and_loses(team_e, team_f, winner_is(team_e.name, team_f.name,
                                                     team_e_score, team_f_score))
    team_g_score, team_h_score = game(team_g.name, team_g.strength,
                                          team_h.name, team_h.strength)
    updates_wins_and_loses(team_g, team_h, winner_is(team_g.name, team_h.name,
                                                     team_g_score, team_h_score))
    team_i_score, team_j_score = game(team_i.name, team_i.strength,
                                          team_j.name, team_j.strength)
    updates_wins_and_loses(team_i, team_j, winner_is(team_i.name, team_j.name,
                                                     team_i_score, team_j_score))
    team_k_score, team_l_score = game(team_k.name, team_k.strength,
                                          team_l.name, team_l.strength)
    updates_wins_and_loses(team_k, team_l, winner_is(team_k.name, team_l.name,
                                                     team_k_score, team_l_score))
    print("---------------------------")
    print_score(team_a.name, team_b.name,
               team_a_score, team_b_score)
    print_score(team_c.name, team_d.name,
               team_c_score, team_d_score)
    print_score(team_e.name, team_f.name,
               team_e_score, team_f_score)
    print_score(team_g.name, team_h.name,
               team_g_score, team_h_score)
    print_score(team_i.name, team_j.name,
               team_i_score, team_j_score)
    print_score(team_k.name, team_l.name,
               team_k_score, team_l_score)
    print()
    print_standings(team_a.name, team_a.wins, team_a.loses,
                    team_b.name, team_b.wins, team_b.loses,
                    team_c.name, team_c.wins, team_c.loses,
                    team_d.name, team_d.wins, team_d.loses,
                    team_e.name, team_e.wins, team_e.loses,
                    team_f.name, team_f.wins, team_f.loses,
                    team_g.name, team_g.wins, team_g.loses,
                    team_h.name, team_h.wins, team_h.loses,
                    team_i.name, team_i.wins, team_i.loses,
                    team_j.name, team_j.wins, team_j.loses,
                    team_k.name, team_k.wins, team_k.loses,
                    team_l.name, team_l.wins, team_l.loses)
    print("---------------------------")
    
def group(team_a, team_b, team_c, team_d, team_e, team_f,
          team_g, team_h, team_i, team_j, team_k, team_l):
    round_1 = round(team_a, team_l, team_b, team_k, team_c, team_j, team_d, team_i, team_e, team_h, team_f, team_g),
    round_2 = round(team_a, team_k, team_l, team_j, team_b, team_i, team_c, team_h, team_d, team_g, team_e, team_f), 
    round_3 = round(team_a, team_j, team_k, team_i, team_l, team_h, team_b, team_g, team_c, team_f, team_d, team_e), 
    round_4 = round(team_a, team_i, team_j, team_h, team_k, team_g, team_l, team_f, team_b, team_e, team_c, team_d), 
    round_5 = round(team_a, team_h, team_i, team_g, team_j, team_f, team_k, team_e, team_l, team_d, team_b, team_c), 
    round_6 = round(team_a, team_g, team_h, team_f, team_i, team_e, team_j, team_d, team_k, team_c, team_l, team_b), 
    round_7 = round(team_a, team_f, team_g, team_e, team_h, team_d, team_i, team_c, team_j, team_b, team_k, team_l), 
    round_8 = round(team_a, team_e, team_f, team_d, team_g, team_c, team_h, team_b, team_i, team_l, team_j, team_k), 
    round_9 = round(team_a, team_d, team_e, team_c, team_f, team_b, team_g, team_l, team_h, team_k, team_i, team_j), 
    round_10 = round(team_a, team_c, team_d, team_b, team_e, team_l, team_f, team_k, team_g, team_j, team_h, team_i), 
    round_11 = round(team_a, team_b, team_c, team_l, team_d, team_k, team_e, team_j, team_f, team_i, team_g, team_h)

def main():
#     team_1 = make_team(team_inputs())
#     team_2 = make_team(team_inputs())
#     team_3 = make_team(team_inputs())
#     team_4 = make_team(team_inputs())
#     team_5 = make_team(team_inputs())
#     team_6 = make_team(team_inputs())
#     team_7 = make_team(team_inputs())
#     team_8 = make_team(team_inputs())
#     team_9 = make_team(team_inputs())
#     team_10 = make_team(team_inputs())
#     team_11 = make_team(team_inputs())
#     team_12 = make_team(team_inputs())
#     team_13 = make_team(team_inputs())
#     team_14 = make_team(team_inputs())
#     team_15 = make_team(team_inputs())
#     team_16 = make_team(team_inputs())
#     team_17 = make_team(team_inputs())
#     team_18 = make_team(team_inputs())
#     team_19 = make_team(team_inputs())
#     team_20 = make_team(team_inputs())
#     team_21 = make_team(team_inputs())
#     team_22 = make_team(team_inputs())
#     team_23 = make_team(team_inputs())
#     team_24 = make_team(team_inputs())

    

    team_1 = Team('Partizan', 50, 0, 0)
    team_2 = Team('FMP', 45, 0, 0)
    team_3 = Team('Krka', 46, 0, 0)
    team_4 = Team('Cibona', 45, 0, 0)
    team_5 = Team('Cedevita Olimpija', 50, 0, 0)
    team_6 = Team('Buducnost', 49, 0, 0)
    team_7 = Team('Crvena Zvezda', 50, 0, 0)
    team_8 = Team('Mornar', 44, 0, 0)
    team_9 = Team('Mega Bemax', 43, 0, 0)
    team_10 = Team('Igokea', 44, 0, 0)
    team_11 = Team('Primorska', 46, 0, 0)
    team_12 = Team('Zadar', 42, 0, 0)
   
    
    print("*******************************")
    print("************ABA LEAGUE************")
    print("*******************************")
    group_1 = group(team_1, team_2, team_3, team_4, team_5, team_6,
                    team_7, team_8, team_9, team_10, team_11, team_12)
    group_2 = group(team_12, team_11, team_10, team_9, team_8, team_7,
                    team_6, team_5, team_4, team_3, team_2, team_1)
   
  
    

    
if __name__ == '__main__':
    main()
