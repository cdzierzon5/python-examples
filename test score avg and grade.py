#Cody Dzierzon
#Test score Average
#9/17/18
def score_avg():
    global avg
    score1 = input("score:")
    score2 = input("score:")
    score3 = input("score:")
    score4 = input("score:")
    score5 = input("score:")
    score6 = input("score:")
    score7 = input("score:")
    score8 = input("score:")
    score9 = input("score:")
    score10 = input("score:")
    sum = float(score1)+float(score2)+float(score3)+float(score4)+float(score5)+float(score6)+float(score7)+float(score8)+float(score9)+float(score10)
    avg = sum/10
    print(avg)
    

def letter_grade():
    if avg>=90:
        print("A")
    elif avg>=80:
        print("B")
    elif avg>=70:
        print("C")
    elif avg>=60:
        print("D")
    elif avg>=50:
        print("F")
    else:
        print("You are very dumb!!! STUDY MORE")
   
    

score_avg()
letter_grade()
