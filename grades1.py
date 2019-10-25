#quizz_grades

def main():
    grades = ["F", "D", "C", "B", "A"]
    ui = int(input("Enter quizz score: "))
    if ui < 60:
        print(grades[0])
    elif ui in range(60, 70):
        print(grades[1])
    elif ui in range(70, 80):
        print(grades[2])
    elif ui in range(80, 90):
        print(grades[3])
    elif ui in range(90, 101):
        print(grades[4])
main()