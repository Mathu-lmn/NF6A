import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = (b**2)-(4*a*c)

if(d > 0):
    root1 = (-b + math.sqrt(d) / (2 * a))
    root2 = (-b - math.sqrt(d) / (2 * a))
    print("Two  real roots are %.2f and %.2f" %(root1, root2))

elif(d == 0):
    root1 = root2 = -b / (2 * a)
    print("One real root is %.2f" %(root1))

elif(d < 0):
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)
    print("Two complex roots are %.2f+%.2f*i and %.2f-%.2f*i" %(root1, imaginary, root2, imaginary))