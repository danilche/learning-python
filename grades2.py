#quizz_grades no if approach

def main():
    a, b, c, d, f = [], [], [], [], [] 
    for j in range(11):
        a.append("A")
    for j in range(10):
        b.append("B")
    for j in range(10):
        c.append("C")
    for j in range(10):
        d.append("D")
    for j in range(60):
        f.append("F")
    
    mast = f + d + c + b + a
    user_input = int(input("Enter your exam score: "))
    print("Your grade is {}".format(mast[user_input]))
main()