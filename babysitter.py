#babysitter

def main():
    
    s_h = int(input("Enter start hour: "))
    s_m = int(input("Enter start minute: "))
    e_h = int(input("Enter end hour: "))
    e_m = int(input("Enter end minute: "))
    
    if s_h < e_h < 21:
        if s_m <= e_m:
            amount = (e_h - s_h) * 2.5 + ((e_m - s_m) * 2.5) / 60
        elif s_m > e_m:
            amount = (e_h - s_h) * 2.5 - ((s_m - e_m) * 2.5) / 60
    elif s_h < e_h == 21:
        amount = (e_h - s_h) * 2.5 - (s_m * 2.5) / 60
    elif e_h > s_h >= 21:
        if s_m <= e_m:
            amount = (e_h - s_h) * 1.75 + ((e_m - s_m) * 1.75) / 60
        elif s_m > e_m:
            amount = (e_h - s_h) * 1.75 - ((s_m - e_m) * 1.75) / 60
    elif s_h <= 21 < e_h:
        amount = ((21 - s_h) * 2.5 - (s_m * 2.5) / 60 
                  + (e_h - 21) * 1.75 + (e_m * 1.75) / 60)
            
    print("Babysitter is to be paid ${:.2f} for her work".format(amount))
    
    
main()
        