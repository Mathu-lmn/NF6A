input_array = [2,5,1,6,4]

sorted_array = sorted(input_array)
print(sorted_array)

# divide the array in two parts
left_array = sorted_array[0:(len(sorted_array)//2+1)]
right_array = sorted_array[(len(sorted_array)+1)//2:]
print(right_array)
output_array = []
# we want the output to alternate between the two parts
for i in range(len(left_array)):
    output_array.append(left_array[i])
    if i < len(right_array):
        output_array.append(right_array[i])

print(output_array)

indices_list = []
# append to the list the indices of the elements from the input array in output array 
for i in range(len(output_array)):
    for j in range(len(input_array)):
        if output_array[i] == input_array[j]:
            indices_list.append(j)
print(indices_list)