#BMI

def BMI_message(BMI):
    
    if BMI < 19:
        print("Your BMI is {:.2f} and you are underweight".format(BMI))
    elif 19 <= BMI <= 25:
        print("Your BMI is {:.2f} and you are normal weight".format(BMI))
    elif 25 < BMI <= 30:
        print("Your BMI is {:.2f} and you are overweight".format(BMI))
    else:
        print("Your BMI is {:.2f} and you are obese".format(BMI))
        

def main():
    
    q = input("Do you want to work with lbs or kg?  "  )
    
    if q == 'lbs':
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        BMI = (weight * 720) / (height * height)
        BMI_message(BMI)
        
    else:
        weight = float(input("Enter your weight in kilos: "))
        height = int(input("Enter your height in centimeters: "))
        BMI = weight / ((height / 100) * (height / 100))
        BMI_message(BMI)
    
    
main()
        