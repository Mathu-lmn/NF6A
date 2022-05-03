list_numbers = []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    new = int(input())
 
    list_numbers.append(new)   
print(list_numbers)


sum = 0
for i in list_numbers:
    sum += i

average = sum / len(list_numbers)

product = 1
for i in list_numbers:
    product *= i


print("The sum of the numbers is:", sum)
print("The average of the numbers is:", average)
print("The product of the numbers is:", product)

number = input("Enter a number: ")
if number in list_numbers:
    print("The number is in the list")
else:
    print("The number is not in the list")

number = int(input("Enter a number: "))
position = int(input("Enter the position of the number in the list: "))

list_numbers.insert(position, number)

print(list_numbers)

number_remove = int(input("Enter the number to remove: "))
if number_remove in list_numbers:
    list_numbers.remove(number_remove)
    print(list_numbers)
else:
    print("The number is not in the list")

slice_i_1 = int(input("Enter the first position of the slice: "))
slice_i_2 = int(input("Enter the second position of the slice: "))

list_numbers_slice = list_numbers[slice_i_1:slice_i_2]

print(list_numbers_slice)