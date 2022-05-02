name = input("What is your name? ")
age = int(input("How old are you? "))
height = int(input("How tall are you? "))

if len(name) > 20:
    print("Your name is long")
elif len(name) > 15:
    print("Your name is semi long")
elif len(name) > 8:
    print("Your name is semi short")
else :
    print("Your name is short")

if age > 18:
    print("You are an adult")
else :
    print("You are not an adult")

if height > 172:
    print("You are tall")
else :
    print("You are not tall")