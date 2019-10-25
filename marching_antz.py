number = [
        "one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine", "ten"
         ]

action = ["suck her thumb", "tie her shoe", "climb a tree", 
          "shut the door", "take a dive", "pick up sticks",
          "pray to heaven", "shut the gate", "check the time", "say 'The End'"
          ]

def verse_1_2(j):
    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(number[j]))
    

def verse_3(j):
    print("The ants go marching {0} by {0},".format(number[j]))
    
def verse_4(j):
    print("The little one stops to {}".format(action[j]))
    
def verse_5():
    print("To get out of the rain, BOOM! BOOM! BOOM!")
    

def main():
    print("Oh, Where, Oh, Where Has My Little Dog Gone?".upper())
    print()
    print()
    
    for j in range(len(number)):
        verse_1_2(j)
        verse_1_2(j)
        verse_3(j)
        verse_4(j)
        verse_5()
        print()
    
main()
        