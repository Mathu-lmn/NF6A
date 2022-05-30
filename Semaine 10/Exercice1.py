content = []
file = open("Semaine 10/first.txt", "r")
for line in file:
    content.append(line)
file.close()

def similarity(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    n = list(dict.fromkeys(set(s1).union(s2)))
    intersection = set(s1)&set(s2)
    return round(len(intersection) / len(n),3)


def similarity_matrix():
    matrix = []
    for i in range(len(content)):
        matrix.append([])
        for j in range(len(content)):
            matrix[i].append(similarity(content[i], content[j]))
    print("The similarity matrix between the sentences is : \n")
    for i in matrix:
        print(*i,sep="\t")

similarity_matrix()

def get_largest_smallest_similarity():
    largest = 0
    large = []
    smallest = 1
    small = []
    for i in range(len(content)):
        for j in range(len(content)):
            if i == j:
                continue
            else:
                if similarity(content[i], content[j]) > largest:
                    largest = similarity(content[i], content[j])
                    large = [i, j]
                if similarity(content[i], content[j]) < smallest:
                    smallest = similarity(content[i], content[j])
                    small = [i, j]
    print("\nThe sentences with the most similarities are:", large)
    print("The sentences with the least similarities are:", small)

get_largest_smallest_similarity()

def average_similarity():
    sum = 0
    for i in range(len(content)):
        for j in range(len(content)):
            if i == j:
                continue
            else:
                sum += similarity(content[i], content[j])
    print("\nThe average degree of similarity of the file is :", round(sum / (len(content) * (len(content) - 1)), 3))

average_similarity()