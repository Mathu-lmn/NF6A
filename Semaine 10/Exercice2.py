Students = []
def grade_input():
    number_students = int(input("How many students do you want to enter? "))
    for i in range(number_students):
        name = input("What is the student's name? ")
        grade = int(input("What is the student's grade? "))
        if grade > 20 or grade < 0:
            print("Grade must be between 0 and 20")
            grade_input()
        Students.append([name,grade])

grade_input()
print("\n")

def class_average():
    total = 0
    for i in range(len(Students)):
        total += Students[i][1]
    average = total / len(Students)
    return average

print("The class average is", class_average())

def class_standard_deviation():
    total = 0
    for i in range(len(Students)):
        total += (Students[i][1] - class_average())**2
    standard_deviation = total / len(Students)
    print("The standard deviation is :",standard_deviation**0.5)

class_standard_deviation()

def lowest_grade():
    lowest = Students[0][1]
    for i in range(len(Students)):
        if Students[i][1] < lowest:
            lowest = Students[i][1]
            name = Students[i][0]
    print(f"{name} has the lowest grade with {lowest}/20")

lowest_grade()

def highest_grade():
    highest = Students[0][1]
    for i in range(len(Students)):
        if Students[i][1] > highest:
            highest = Students[i][1]
            name = Students[i][0]
    print(f"{name} has the highest grade with {highest}/20")

def get_student_ranking():
    name = input("What is the student's name? ")
    Students.sort(key=lambda x: x[1])
    for i in range(len(Students)):
        if Students[i][0] == name:
            print(f"{name} is ranked {i+1}/{len(Students)}")
            return
    print("This student is not in the class")
    get_student_ranking()

get_student_ranking()

def modify_grades():
    name = input("What is the student's name? ")
    for i in range(len(Students)):
        if Students[i][0] == name:
            grade = int(input("What is the student's new grade? "))
            if grade > 20 or grade < 0:
                print("Grade must be between 0 and 20")
                modify_grades()
            Students[i][1] = grade
            print("The student's grade has been modified")
            return
    print("This student is not in the class")
    modify_grades()