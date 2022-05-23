content = []
file = open("Semaine 10/first.txt", "r")
for line in file:
    content.append(line)
file.close()
print(content)