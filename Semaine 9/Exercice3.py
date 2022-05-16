first = int(input("Enter the first term of the series : "))
r = int(input("Enter the common ratio : "))
n = int(input("Enter the number of terms : "))

def n_element():
    result = first * r**(n-1)
    print("The", n, "th element of the series is : ", result)

n_element()

def n_list():
    a = first
    for i in range(n):
        print(a, end=" ")
        a = a * r
        
n_list()

def sum_elements():
    value = first
    total = 0
    for i in range(n):
        total = total + value
        value = value * r
    print("\nThe sum of the series is : ", total)

# sum_elements()

def sum_elements2():
    total = int((first * (1 - r**n)) / (1 - r))
    print("The sum of the series is : ", total)

sum_elements2()

def is_geometric():
    list = []
    num = int(input("Enter the size of the list : "))
    for i in range(num):
        list.append(int(input("Enter the next number : ")))
    
    ratio = list[1]/float(list[0])
    for i in range(1, len(list)):
        if list[i]/float(list[i-1]) != ratio:
            print("The series is not geometric")
            return
    print("The series is geometric and has a ratio of : ", ratio)

is_geometric()