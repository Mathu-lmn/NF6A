from sympy import *

number = int(input("Enter a number: "))

if number < 0:
    print("The number is negative")
elif number > 0:
    print("The number is positive")
else:
    print("The number is zero")

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


if isprime(number):
    print("The number is prime")
else:
    print("The number is not prime")


numbers = [int(input("Enter a number: ")) for i in range(10)]

even = 0
odd = 0
prime = 0

for i in numbers:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
    if isprime(i):
        prime+=1

print("The number of even numbers is", even)
print("The number of odd numbers is", odd)
print("The number of prime numbers is", prime)