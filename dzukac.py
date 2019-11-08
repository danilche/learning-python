# gsa.py
#    Program to find footbal player with highest goal scoring percentage

class Player:

    def __init__(self, name, goals, games):
        self.name = name
        self.goals = int(goals)
        self.games = int(games)

    def getName(self):
        return self.name

    def getGames(self):
        return self.games

    def getGoals(self):
        return self.goals

    def gsa(self):
        return self.goals/self.games

def makePlayer(infoStr):
    # infoStr is a tab-separated line: name goals games
    # returns a corresponding Player object
    name, goals, games = infoStr.split(",")
    return Player(name, goals, games)

def main():
    # open the input file for reading
    with open('/home/dane/wrangling/liverpool.txt', 'r') as infile:

    # set best to the record for the first player in the file
        best = makePlayer(infile.readline())

    # process subsequent lines of the file
        for line in infile:
        # turn the line into a player record
            s = makePlayer(line)
        # if this player is best so far, remember it.
            if s.gsa() > best.gsa():
                best = s


    # print information about the best player
    print("The best player is:", best.getName())
    print("games:", best.getGames())
    print("goals:", best.getGoals())
    print("GSA: {:.2f}".format(best.gsa()))

if __name__ == '__main__':
    main()
