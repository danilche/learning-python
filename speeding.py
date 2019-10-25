#speeding

def regular_fine(speed, limit):
    fine = 50 + (speed - limit) * 5
    return fine

def over_90_fine(speed, limit):
    fine = 50 + (speed - limit) * 5 + 200
    return fine    

def main():
    
    limit = int(input("Enter speed limit: "))
    speed = int(input("Enter achieved speed: "))
    
    if speed <= limit:
        print("Thank you for driving carefully!")
    elif limit > 90:
        print("You have to pay ${} fine for speeding"\
              .format(over_90_fine(speed, limit)))
    else:
        if speed > 90:
            print("You have to pay ${} fine for speeding"\
                  .format(over_90_fine(speed, limit)))
        else:
            print("You have to pay ${} fine for speeding"\
                  .format(over_90_fine(speed, limit)))
    
main()
        