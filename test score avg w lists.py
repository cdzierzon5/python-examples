#cody d
#12-4-18
#avg grades

gradelist =[]
def getGrade(gradelist):

    while True:
        maxGrade = 100
        grade= input("enter in a grade, to exit press space bar")
        if grade == " ":
            break
        elif grade.isdigit():
            grade = float(grade)
            if grade <= maxGrade:
                gradelist.append(grade)
            else:
                q = input("are you sure this "+str(grade)+"is a good grade y or n")
                if q == "y":
                    gradelist.append(grade)
                else:
                    print("that's not a good grade")
        else:
            print("that is not a valid grade")

def avgfunction(gradelist):
    total = 0
    for grade in gradelist:
        total += grade
    avg = total / len(gradelist)
    return avg

def main(gradelist):

    getGrade(gradelist)
    avg = avgfunction(gradelist)
    xmax = max(gradelist)
    xmin = min(gradelist)
    print(xmax)
    print(xmin)
    print("yaur grade is", avg)

main(gradelist)

    
