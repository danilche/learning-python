import math

def pizzaArea(r):
    a = r*r * math.pi
    return a

def pizzaCost(a, p):
    cpcm = p / a
    return cpcm


def main():
    diameter = float(input("Enter diameter of the pizza: "))
    price = float(input("Enter price of the pizza: "))
    area = pizzaArea(diameter)
    cost_per_sqcm = pizzaCost(area, price)
    area_i = area * 0.393701
    cost_per_sqi = pizzaCost(area_i, price)
    print("The price of your pizza is ${:0.3f} per square centimeter and \
${:0.3f} per square inch".format(cost_per_sqcm, cost_per_sqi))
    
main()
    