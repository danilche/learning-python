### Print all states that have "la" in name
def find_la(states):
    for state in states:
        if "la" in state:
            print(state)

### Print all US states with name consisting of two or more words
def two_or_more_words(states):
    for state in states:
        if " " in state:
            print(state)
            
### Print all US states with name shorter than 6 letters
def shorter_than_six(states):
    for state in states:
        if len(state) < 6:
            print(state)

### Prints all US states name starting with 'P' or ending with 'y' (dakle, 'py' :) 
def starts_with_p_ends_with_y(states):
    for state in states:
        if state[0] == "P" or state[-1] == "y":
            print(state)

def main():

    us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
               'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
               'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
               'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
               'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
               'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
               'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
               'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
               'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 
               'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    
    print()
    print("US states with 'la' in name:")
    print()
    find_la(us_states)
    print("######################")
    print()
    print("US states with name consisting of two or more words:")
    print()
    two_or_more_words(us_states)
    print("######################")
    print()
    print("US states with name shorter than 6 letters:")
    print()
    shorter_than_six(us_states)
    print("######################")
    print()
    print("US states name starting with 'P' or ending with 'y':")
    print()
    starts_with_p_ends_with_y(us_states)
    print("######################")
    
main()


        
