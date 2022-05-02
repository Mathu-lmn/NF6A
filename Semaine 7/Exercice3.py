password = input("Enter a password: ")

upper = lower = digit = special = 0

for i in range(len(password)):
    if password[i].isupper():
        upper+=1
    elif password[i].islower():
        lower+=1
    elif password[i].isdigit(): 
        digit+=1
    else:
        special+=1

if upper < 2:
    print("The password must contain at least 2 uppercase letters")
elif lower < 2:
    print("The password must contain at least 2 lowercase letters")
elif digit < 2:
    print("The password must contain at least 2 digits")
elif special < 1:
    print("The password must contain at least 1 special character")
elif len(password) < 6:
    print("The password must be at least 6 characters long")
elif len(password) > 16:
    print("The password must be at most 16 characters long")
else:
    print("The password is valid")