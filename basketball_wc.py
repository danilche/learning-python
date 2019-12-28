#this is work in progress

from random import *

class Team:

    def __init__(self, name, strength, wins, loses, score_for, score_against):
        self.name = name
        self.strength = float(strength)
        self.wins = int(wins)
        self.loses = int(loses)
        self.score_for = int(score_for)
        self.score_against = int(score_against)

    def getName(self):
        return self.name

    def getStrength(self):
        return self.strength

    def getWins(self):
        return self.wins
    
    def updateWins(self):
        self.wins = self.wins + 1

    def getLoses(self):
        return self.loses
    
    def updateLoses(self):
        self.loses = self.loses + 1
        
    def updatePointsFor(self, points_for):
        self.score_for += points_for 
        
    def updatePointsAgainst(self, points_against):
        self.score_against += points_against
 
def score_loop(strength, number_of_loops):
    score = 0
    for j in range(number_of_loops):    
        if random() <= strength/ 100:
            score = score + 1
        else:
            pass
    return score

def game(team_a, team_b):    
    score_a = score_loop(team_a.strength, 160) 
    score_b = score_loop(team_b.strength, 160)
    while score_a == score_b:
        ot_a = score_loop(team_a.strength, 30)
        ot_b = score_loop(team_b.strength, 30)
        score_a = score_a + ot_a
        score_b = score_b + ot_b
    return score_a, score_b

def is_winner(team_a, team_b,
              score_a, score_b):
    if score_a > score_b:
        winner = team_a
    else:
        winner = team_b
    return winner

def is_loser(team_a, team_b,
              score_a, score_b):
    if score_a < score_b:
        loser = team_a
    else:
        loser = team_b
    return loser

def updates_wins_and_loses(team_a, team_b, winner):
    if winner == team_a:
        team_a.updateWins(), team_b.updateLoses()
    else:
        team_b.updateWins(), team_a.updateLoses()

def update_points_for_against(team_a, team_b, score_a, score_b):
    team_a.updatePointsFor(score_a)
    team_a.updatePointsAgainst(score_b)
    team_b.updatePointsFor(score_b)
    team_b.updatePointsAgainst(score_a)

        
def print_score(team_a, team_b, score_a, score_b):
    print("{} - {}    {}:{}".format(team_a.name, team_b.name, score_a, score_b))   

def group_winners(team_a, team_b, team_c, 
                    team_d, team_e, team_f):
    pool_wins = {team_a.name:team_a.wins, team_b.name:team_b.wins,
                 team_c.name:team_c.wins, team_d.name:team_d.wins,
                 team_e.name:team_e.wins, team_f.name:team_f.wins}
    wins = sorted(pool_wins.values(), reverse=True)
    teams = sorted(pool_wins, key=pool_wins.get, reverse=True)
    winners = []
    new_teams = []
    score_diff = []
    for j in range(6):
        if teams[j] == team_a.name:
            new_teams.append(team_a)
            score_diff.append(team_a.score_for - team_a.score_against)
        elif teams[j] == team_b.name:
            new_teams.append(team_b)
            score_diff.append(team_b.score_for - team_b.score_against)
        elif teams[j] == team_c.name:
            new_teams.append(team_c)
            score_diff.append(team_c.score_for - team_c.score_against)
        elif teams[j] == team_d.name:
            new_teams.append(team_d)
            score_diff.append(team_d.score_for - team_d.score_against)
        elif teams[j] == team_e.name:
            new_teams.append(team_e)
            score_diff.append(team_e.score_for - team_e.score_against)
        else:
            new_teams.append(team_f)
            score_diff.append(team_f.score_for - team_f.score_against)
    if new_teams[0].wins == 5 and wins.count(4) == 1:
        winners.append(new_teams[0])
        winners.append(new_teams[1])
    elif new_teams[0].wins == 5 and wins.count(3) == 1:
        winners.append(new_teams[0])
        winners.append(new_teams[1])
    elif new_teams[0].wins == 5 and wins.count(3) == 2:
        winners.append(new_teams[0])
        for j in range(1, 3):
            if score_diff[j] == max(score_diff[1], score_diff[2]):
                winners.append(new_teams[j])
            else:
                pass
    elif new_teams[0].wins == 5 and wins.count(3) == 3:
        winners.append(new_teams[0])
        for j in range(1, 4):
            if score_diff[j] == max(score_diff[1], score_diff[2], score_diff[3]):
                winners.append(new_teams[j])
            else:
                pass
    elif new_teams[0].wins == 5 and wins.count(2) == 5:
        winners.append(new_teams[0])
        for j in range(1, 6):
            if score_diff[j] == max(score_diff[1], score_diff[2], score_diff[3], score_diff[4], score_diff[5]):
                winners.append(new_teams[j])
            else:
                pass
    elif new_teams[0].wins == 4 and wins.count(4) == 1 and wins.count(3) == 1:
        winners.append(new_teams[0])
        winners.append(new_teams[1])
    elif new_teams[0].wins == 4 and wins.count(4) == 1 and wins.count(3) == 2:
        winners.append(new_teams[0])
        for j in range(1, 3):
            if score_diff[j] == max(score_diff[1], score_diff[2]):
                winners.append(new_teams[j])
            else:
                pass
    elif new_teams[0].wins == 4 and wins.count(4) == 1 and wins.count(3) == 3:
        winners.append(new_teams[0])
        for j in range(1, 4):
            if score_diff[j] == max(score_diff[1], score_diff[2], score_diff[3]):
                winners.append(new_teams[j])
            else:
                pass
    elif new_teams[0].wins == 4 and wins.count(4) == 2:
        if score_diff[0] >= score_diff[1]:
            winners.append(new_teams[0])
            winners.append(new_teams[1])
        else:
            winners.append(new_teams[1])
            winners.append(new_teams[0])
    elif new_teams[0].wins == 4 and wins.count(4) == 3:
        get_max = [score_diff[0], score_diff[1], score_diff[2]]
        while len(winners) < 2:
            for j in range(3):
                if score_diff[j] == max(get_max):
                    winners.append(new_teams[j])
                    get_max.remove(max(get_max))
                else:
                    pass
    elif new_teams[0].wins == 3 and wins.count(3) == 3:
        get_max = [score_diff[0], score_diff[1], score_diff[2]]
        while len(winners) < 2:
            for j in range(3):
                if score_diff[j] == max(get_max):
                    winners.append(new_teams[j])
                    get_max.remove(max(get_max))
                else:
                    pass
    elif new_teams[0].wins == 3 and wins.count(3) == 4:
        get_max = [score_diff[0], score_diff[1], score_diff[2], score_diff[3]]
        while len(winners) < 2:
            for j in range(4):
                if score_diff[j] == max(get_max):
                    winners.append(new_teams[j])
                    get_max.remove(max(get_max))
                else:
                    pass
    elif new_teams[0].wins == 3 and wins.count(3) == 5:
        get_max = [score_diff[0], score_diff[1], score_diff[2], score_diff[3], score_diff[4]]
        while len(winners) < 2:
                for j in range(5):
                    if score_diff[j] == max(get_max):
                        winners.append(new_teams[j])
                        get_max.remove(max(get_max))
                    else:
                        pass
    else:
        print("Have no idea what went wrong!")
    winners = winners[:2]
    return winners
    
def print_standings(team_a, team_b, team_c, 
                    team_d, team_e, team_f):
    pool_wins = {team_a.name:team_a.wins, team_b.name:team_b.wins,
                 team_c.name:team_c.wins, team_d.name:team_d.wins,
                 team_e.name:team_e.wins, team_f.name:team_f.wins}
    pool_loses = {team_a:team_a.loses, team_b:team_b.loses,
                 team_c:team_c.loses, team_d:team_d.loses,
                 team_e:team_e.loses, team_f:team_f.loses}
    wins = sorted(pool_wins.values(), reverse=True)
    loses = sorted(pool_loses.values())
    teams = sorted(pool_wins, key=pool_wins.get, reverse=True)
    sep = "  "
    winners = []
    print()
    print("Standings:")
    print()
    for j in range(6):
        if teams[j] == team_a.name:
            print("{}{}{}-{}  {}:{} ({})".format(teams[j].ljust(12), sep, wins[j], loses[j], 
                                 team_a.score_for, team_a.score_against,
                                 team_a.score_for - team_a.score_against))
        elif teams[j] == team_b.name:
            print("{}{}{}-{}  {}:{} ({})".format(teams[j].ljust(12), sep, wins[j], loses[j], 
                                 team_b.score_for, team_b.score_against,
                                 team_b.score_for - team_b.score_against))
        elif teams[j] == team_c.name:
            print("{}{}{}-{}  {}:{} ({})".format(teams[j].ljust(12), sep, wins[j], loses[j], 
                                 team_c.score_for, team_c.score_against,
                                 team_c.score_for - team_c.score_against))
        elif teams[j] == team_d.name:
            print("{}{}{}-{}  {}:{} ({})".format(teams[j].ljust(12), sep, wins[j], loses[j], 
                                 team_d.score_for, team_d.score_against,
                                 team_d.score_for - team_d.score_against))
        elif teams[j] == team_e.name:
            print("{}{}{}-{}  {}:{} ({})".format(teams[j].ljust(12), sep, wins[j], loses[j], 
                                 team_e.score_for, team_e.score_against,
                                 team_e.score_for - team_e.score_against))
        else:
            print("{}{}{}-{}  {}:{} ({})".format(teams[j].ljust(12), sep, wins[j], loses[j], 
                                 team_f.score_for, team_f.score_against,
                                 team_f.score_for - team_f.score_against))
    return winners
        
def roundz(team_a, team_b, team_c, team_d, team_e, team_f):    
    score_a, score_b = game(team_a, team_b)
    updates_wins_and_loses(team_a, team_b, is_winner(team_a, team_b,
                                                     score_a, score_b))
    update_points_for_against(team_a, team_b, score_a, score_b)
    score_c, score_d = game(team_c, team_d)
    updates_wins_and_loses(team_c, team_d, is_winner(team_c, team_d,
                                                     score_c, score_d))
    update_points_for_against(team_c, team_d, score_c, score_d)
    score_e, score_f = game(team_e, team_f)
    updates_wins_and_loses(team_e, team_f, is_winner(team_e, team_f,
                                                     score_e, score_f))
    update_points_for_against(team_e, team_f, score_e, score_f)
    print("---------------------------")
    print_score(team_a, team_b,
               score_a, score_b)
    print_score(team_c, team_d,
               score_c, score_d)
    print_score(team_e, team_f,
               score_e, score_f)
    print()
    print_standings(team_a, team_b, team_c,
                    team_d, team_e, team_f)
    print("---------------------------")
    
def group(team_a, team_b, team_c, team_d, team_e, team_f):
    round_1 = roundz(team_a, team_b, team_c, team_d, team_e, team_f)
    round_2 = roundz(team_a, team_c, team_b, team_e, team_d, team_f)
    round_3 = roundz(team_a, team_d, team_b, team_f, team_c, team_e)
    round_4 = roundz(team_a, team_e, team_b, team_d, team_c, team_f)
    round_5 = roundz(team_a, team_f, team_b, team_c, team_d, team_e)

def main():

    team_1 = Team('USA', 59, 0, 0, 0, 0)
    team_2 = Team('Greece', 48, 0, 0, 0, 0)
    team_3 = Team('Lithuania', 50, 0, 0, 0, 0)
    team_4 = Team('Croatia', 43, 0, 0, 0, 0)
    team_5 = Team('Angola', 39, 0, 0, 0, 0)
    team_6 = Team('New Zealand', 40, 0, 0, 0, 0)
    #######################################
    team_7 = Team('France', 53, 0, 0, 0, 0)
    team_8 = Team('Italy', 48, 0, 0, 0, 0)
    team_9 = Team('Canada', 45, 0, 0, 0, 0)
    team_10 = Team('Germany', 44, 0, 0, 0, 0)
    team_11 = Team('Senegal', 40, 0, 0, 0, 0)
    team_12 = Team('China', 36, 0, 0, 0, 0)
    ######################################
    team_13 = Team('Spain', 52, 0, 0, 0, 0)
    team_14 = Team('Russia', 46, 0, 0, 0, 0)
    team_15 = Team('Argentina', 49, 0, 0, 0, 0)
    team_16 = Team('Czech Republic', 43, 0, 0, 0, 0)
    team_17 = Team('Nigeria', 40, 0, 0, 0, 0)
    team_18 = Team('Iran', 39, 0, 0, 0, 0)
    #######################################
    team_19 = Team('Serbia', 52, 0, 0, 0, 0)
    team_20 = Team('Australia', 51, 0, 0, 0, 0)
    team_21 = Team('Slovenia', 46, 0, 0, 0, 0)
    team_22 = Team('Brazil', 46, 0, 0, 0, 0)
    team_23 = Team('Japan', 38, 0, 0, 0, 0)
    team_24 = Team('Puerto Rico', 40, 0, 0, 0, 0)
    

    print("*******************************")
    print("************GROUP A************")
    print("*******************************")
    group_A = group(team_1, team_2, team_3, team_4, team_5, team_6)
    print("*******************************")
    print("************GROUP B************")
    print("*******************************")
    group_B = group(team_7, team_8, team_9, team_10, team_11, team_12)
    print("*******************************")
    print("************GROUP C************")
    print("*******************************")
    group_C = group(team_13, team_14, team_15, team_16, team_17, team_18)
    print("*******************************")
    print("************GROUP D************")
    print("*******************************")
    group_D = group(team_19, team_20, team_21, team_22, team_23, team_24)
    
    
    
    
    winner_A1, winner_A2 = group_winners(team_1, team_2, team_3, 
                                         team_4, team_5, team_6)
    winner_B1, winner_B2 = group_winners(team_7, team_8, team_9, 
                                         team_10, team_11, team_12)
    winner_C1, winner_C2 = group_winners(team_13, team_14, team_15,
                                         team_16, team_17, team_18)
    winner_D1, winner_D2 = group_winners(team_19, team_20, team_21,
                                         team_22, team_23, team_24)
    print("*******************************")
    print("************QUARTER-FINALS************")
    print("*******************************")
    score_A1, score_B2 = game(winner_A1, winner_B2)
    score_B1, score_A2 = game(winner_B1, winner_A2)
    score_C1, score_D2 = game(winner_C1, winner_D2)
    score_D1, score_C2 = game(winner_D1, winner_C2)
    winner_A1B2 = is_winner(winner_A1, winner_B2, score_A1, score_B2)
    winner_B1A2 = is_winner(winner_B1, winner_A2, score_B1, score_A2)
    winner_C1D2 = is_winner(winner_C1, winner_D2, score_C1, score_D2)
    winner_D1C2 = is_winner(winner_D1, winner_C2, score_D1, score_C2) 
    print("{} - {} {}:{}".format(winner_A1.name, winner_B2.name, score_A1, score_B2))
    print("{} - {} {}:{}".format(winner_B1.name, winner_A2.name, score_B1, score_A2))
    print("{} - {} {}:{}".format(winner_C1.name, winner_D2.name, score_C1, score_D2))
    print("{} - {} {}:{}".format(winner_D1.name, winner_C2.name, score_D1, score_C2))
    print("*******************************")
    print("************SEMI-FINALS************")
    print("*******************************")
    score_A1B2, score_C1D2 = game(winner_A1B2, winner_C1D2)
    score_B1A2, score_D1C2 = game(winner_B1A2, winner_D1C2)
    winner_A1B2_C1D2 = is_winner(winner_A1B2, winner_C1D2, score_A1B2, score_C1D2)
    winner_B1A2_D1C2 = is_winner(winner_B1A2, winner_D1C2, score_B1A2, score_D1C2)
    loser_A1B2_C1D2 = is_loser(winner_A1B2, winner_C1D2, score_A1B2, score_C1D2)
    loser_B1A2_D1C2 = is_loser(winner_B1A2, winner_D1C2, score_B1A2, score_D1C2)
    print("{} - {} {}:{}".format(winner_A1B2.name, winner_C1D2.name, score_A1B2, score_C1D2))
    print("{} - {} {}:{}".format(winner_B1A2.name, winner_D1C2.name, score_B1A2, score_D1C2))
    print("*******************************")
    print("************3RD PLACE************")
    print("*******************************")
    score_loser_A1B2_C1D2, score_loser_B1A2_D1C2 = game(loser_A1B2_C1D2, loser_B1A2_D1C2)
    bronze_medalist = is_winner(loser_A1B2_C1D2, loser_B1A2_D1C2, 
                                score_loser_A1B2_C1D2, score_loser_B1A2_D1C2)
    print("{} - {} {}:{}".format(loser_A1B2_C1D2.name, loser_B1A2_D1C2.name,
                                 score_loser_A1B2_C1D2, score_loser_B1A2_D1C2))
    print("Bronze medal is won by {}".format(bronze_medalist.name))
    print("*******************************")
    print("************FINAL************")
    print("*******************************")
    score_winner_A1B2_C1D2, score_winner_B1A2_D1C2 =  game(winner_A1B2_C1D2, winner_B1A2_D1C2)
    champ = is_winner(winner_A1B2_C1D2, winner_B1A2_D1C2, 
                      score_winner_A1B2_C1D2, score_winner_B1A2_D1C2)
    print("{} - {} {}:{}".format(winner_A1B2_C1D2.name, winner_B1A2_D1C2.name, 
                                 score_winner_A1B2_C1D2, score_winner_B1A2_D1C2))
    print("{} is the world champion!!!".format(champ.name))
    
if __name__ == '__main__':
    main()