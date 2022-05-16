import random

Words_definition = {
    "work" : "to do something",
    "school" : "a place where you learn",
    "home" : "the place where you live",
    "computer" : "a device that you use to do something",
    "program" : "a set of instructions that you give to a computer",
    "python" : "a programming language",
    "science" : "the study of something",
    "math" : "the study of numbers",
    "physics" : "the study of matter",
    "chair" : "a piece of furniture that you can sit on",
    "wifi" : "a network that you can use to connect to the internet",
    "door" : "a piece of furniture that you can open or close",
    "wood" : "a type of material that you can use to make things",
}

def get_random_word():
    random_word = random.choice(list(Words_definition.keys()))
    print("The word is:", random_word, "and its definition is:", Words_definition[random_word])

# get_random_word()

def guess_word(live):
    random_word = random.choice(list(Words_definition.keys()))
    size = len(random_word)
    print("You have",live,"lives left")
    print("The word has", size, "letters and means:", Words_definition[random_word])
    while live > 0:
        guess = input("Guess the word: ").casefold()
        if guess == random_word:
            print("You won!")
            live += 1
            guess_word(live)
        else:
            print("You lost!")
            live = live - 1
            print("You have", live, "lives left")
            if live == 0:
                print("You lost the game!")
                break

live = 3
guess_word(live)