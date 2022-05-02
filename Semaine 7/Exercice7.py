text = input("Enter a text: ")

list = text.split()
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowel_count1 = 0
vowel_count = 0
words_with_2_or_more_vowels = 0

print("The number of words is:", len(list))
for i in range(len(text)):
    if text[i] in vowel:
        vowel_count1 += 1

for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] in vowel:
            vowel_count += 1
    
    if vowel_count >= 2:
        words_with_2_or_more_vowels += 1
        vowel_count = 0
    else:
        vowel_count = 0

print("The number of vowels is:", vowel_count1)

print("There are {} words with 2 or more vowels".format(words_with_2_or_more_vowels))