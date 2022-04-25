import math
r = int(input("\nEnter the radius of the cone: "))
h = int(input("\nEnter the height of the cone: "))

b = math.pi*r*r

print("\nThe are of the circular base is: ", b)

v = (1/3)*(3.14)*(r**2)*h

print("\nThe volume of the cone is: ", v)