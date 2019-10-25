from random import *

def inputs():
          
    name = input("Enter team name: ")
    strength = int(input("Enter team strength on scale 1 - 100: "))
    return name, strength

def normal_set(strength_a, strength_b):
    score_a = 0
    score_b = 0
    serving = "A"
    while not ((score_a >= 25 or score_b >= 25) 
                and (abs(score_a - score_b) >= 2)):
        if serving == "A":
            if random() < strength_a / 100:
                score_a += 1
            else:
                serving = "B"
        else: 
            if random() < strength_b / 100:
                score_b += 1
            else:
                serving = "A"
    return score_a, score_b

def tie_break(strength_a, strength_b):
    score_a = 0
    score_b = 0
    serving = "A"
    while not ((score_a >= 15 or score_b >= 15) 
                and (abs(score_a - score_b) >= 2)):
        if serving == "A":
            if random() < strength_a / 100:
                score_a += 1
            else:
                serving = "B"
        else: 
            if random() < strength_b / 100:
                score_b += 1
            else:
                serving = "A"
    return score_a, score_b

def result(result_a, result_b, score_a, score_b):
    if score_a > score_b:
        result_a.append(1)
    else:
        result_b.append(1)
    return result_a, result_b

def main():
    result_a = []
    result_b = []
    name_a, strength_a = inputs()
    name_b, strength_b = inputs()
    first_set = normal_set(strength_a, strength_b)
    result(result_a, result_b, first_set[0], first_set[1])
    second_set = normal_set(strength_a, strength_b)
    result(result_a, result_b, second_set[0], second_set[1])
    third_set = normal_set(strength_a, strength_b)
    result(result_a, result_b, third_set[0], third_set[1])
    if sum(result_a) == 3 or sum(result_b) == 3:
        print("{} - {} {}:{}".format(name_a, name_b, sum(result_a),
              sum(result_b)))
        print("({}:{}, {}:{}, {}:{})".format
              (first_set[0], first_set[1],
              second_set[0], second_set[1], 
              third_set[0], third_set[1]))
    else:
        fourth_set = normal_set(strength_a, strength_b)
        result(result_a, result_b, fourth_set[0], fourth_set[1])
        if sum(result_a) == 3 or sum(result_b) == 3:
            print("{} - {} {}:{}".format(name_a, name_b, sum(result_a),
                  sum(result_b)))
            print("({}:{}, {}:{}, {}:{}, {}:{})".format
                  (first_set[0], first_set[1],
                   second_set[0], second_set[1],
                   third_set[0], third_set[1],
                   fourth_set[0], fourth_set[1]))
        else:
            fifth_set = tie_break(strength_a, strength_b)
            result(result_a, result_b, fifth_set[0], fifth_set[1])
            print("{} - {} {}:{}".format(name_a, name_b, sum(result_a),
                  sum(result_b)))
            print("({}:{}, {}:{}, {}:{}, {}:{}, {}:{})".format
                  (first_set[0], first_set[1],
                  second_set[0], second_set[1], 
                  third_set[0], third_set[1],
                  fourth_set[0], fourth_set[1], 
                  fifth_set[0], fifth_set[1]))
            
main()
    