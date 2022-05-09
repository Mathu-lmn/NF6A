Students = []
def add_students():
    number_of_students = int(input("Enter the number of new students: "))
    for i in range(number_of_students):
        student = input("\nEnter the name of the student: ")
        print("Enter the grades for the C project: ")
        c_demonstration_grade = input("Enter the demonstration grade: ")
        c_code_grade = input("Enter the code grade: ")
        c_presentation_grade = input("Enter the presentation grade: ")
        c_documentation_grade = input("Enter the documentation grade: ")
        print("Enter the grades for the Python project: ")
        python_demonstration_grade = input("Enter the demonstration grade: ")
        python_code_grade = input("Enter the code grade: ")
        python_presentation_grade = input("Enter the presentation grade: ")
        python_documentation_grade = input("Enter the documentation grade: ")

        c_dict = dict(demonstration=c_demonstration_grade, code=c_code_grade, presentation=c_presentation_grade, documentation=c_documentation_grade)
        python_dict = dict(demonstration=python_demonstration_grade, code=python_code_grade, presentation=python_presentation_grade, documentation=python_documentation_grade)
        student_dict = dict(student=student, c=c_dict, python=python_dict)
        Students.append(student_dict)

add_students()
# print(Students)

def average_grade_per_project():
    for i in range(len(Students)):
        c_average_grade = (int(Students[i]['c']['demonstration']) + int(Students[i]['c']['code']) + int(Students[i]['c']['presentation']) + int(Students[i]['c']['documentation'])) / 4
        python_average_grade = (int(Students[i]['python']['demonstration']) + int(Students[i]['python']['code']) + int(Students[i]['python']['presentation']) + int(Students[i]['python']['documentation'])) / 4
        print(f"\nAverage grades for {Students[i]['student']}:\nC: {c_average_grade}\nPython: {python_average_grade}")

average_grade_per_project()

def average_for_project():
    project = input("Enter the name of the project ('c' or 'python'): ")
    average_grade = 0
    for i in range(len(Students)):
        if project == 'c':
            average_grade += int(Students[i]['c']['demonstration']) + int(Students[i]['c']['code']) + int(Students[i]['c']['presentation']) + int(Students[i]['c']['documentation'])
        elif project == 'python':
            average_grade += int(Students[i]['python']['demonstration']) + int(Students[i]['python']['code']) + int(Students[i]['python']['presentation']) + int(Students[i]['python']['documentation'])
    average_grade = average_grade / len(Students)
    print(f"\nAverage grade for {project}: {average_grade}")

average_for_project()

def correction_weighting():
    c_average_grade = 0
    python_average_grade = 0
    for i in range(len(Students)):
        c_average_grade += (int(Students[i]['c']['demonstration']) + int(Students[i]['c']['code']) + int(Students[i]['c']['presentation']) + int(Students[i]['c']['documentation'])) / 4
        python_average_grade += (int(Students[i]['python']['demonstration']) + int(Students[i]['python']['code']) + int(Students[i]['python']['presentation']) + int(Students[i]['python']['documentation'])) / 4
    if c_average_grade > python_average_grade:
        coeff = (c_average_grade - python_average_grade) / 2
        print(f"\nCorrection weighting: {coeff}")
        print(f"\nAverage before correction: C = {c_average_grade} and Python = {python_average_grade}")
        print(f"\nAverage after correction: C = {c_average_grade - coeff} and Python = {python_average_grade + coeff}")
    elif c_average_grade < python_average_grade:
        coeff = (python_average_grade - c_average_grade) / 2
        print(f"\nCorrection weighting: {coeff}")
        print(f"\nAverage before correction: C = {c_average_grade} and Python = {python_average_grade}")
        print(f"\nAverage after correction: C = {c_average_grade + coeff} and Python = {python_average_grade - coeff}")
    else:
        print("\nNo correction weighting needed")