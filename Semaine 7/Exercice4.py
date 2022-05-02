from random import randint


number = randint(1, 100)

print("I'm thinking of a number between 1 and 100")
guessed = False
guesses = 0
while not guessed:
    guess = int(input("What is your guess? "))
    guesses+=1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("You guessed the number in", guesses, "guesses")
        guessed = True
