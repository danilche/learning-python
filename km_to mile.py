# converting kilometers to miles


def kilo_to_mile():
    kilometer = eval(input("Input distance in kilometers: "))
    mile = kilometer * 0.621371
    print("------------------------------------")
    print("Distance in miles is", mile, "miles")
    for j in range(10):
        print()
    input("Press <Enter> to exit")


kilo_to_mile()