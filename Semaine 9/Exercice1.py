word = input("Enter the word to check : ")
word = word.casefold()

def ispalindrome_iterative(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[-i-1]:
            return False
    return True

def ispalindrome_recursive(str):
    if len(str) < 2:
        return True
    elif str[0] != str[-1]:
        return False
    else:
        return ispalindrome_recursive(str[1:-1])

answer = ispalindrome_recursive(word)

if answer:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")