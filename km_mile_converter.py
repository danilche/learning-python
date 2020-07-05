def mile_to_km(distance):
    km = distance * 1.60934
    return km

def km_to_mile(distance):
    mile = distance * 0.621371
    return mile

def main():
    distance = float(input("Enter your distance: "))
    mile_or_km = str(input("Miles or kilometers (m or km): "))
    if mile_or_km == "m":
        print("Your distance is", mile_to_km(distance), "kilometers.")
    else:
        print("Your distance is", km_to_mile(distance), "miles.")

main()
    
    