def type(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        print("The triangle is equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")

def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    s = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    print("The area of the triangle is : ", s)

def perimeter(side1, side2, side3):
    s = side1 + side2 + side3
    print("The perimeter of the triangle is : ", s)

def user_menu(side1, side2, side3):
    print("""
    1. Type of triangle
    2. Area of triangle
    3. Perimeter of triangle
    4. Quit
    """)
    option = int(input("Enter your choice : "))
    if option == 1:
        type(side1, side2, side3)
    elif option == 2:
        area(side1, side2, side3)
    elif option == 3:
        perimeter(side1, side2, side3)
    elif option == 4:
        exit()
