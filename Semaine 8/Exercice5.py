from tracemalloc import stop
import numpy as np

#####################
# Vector operations #
#####################

def input_vector():
    vector_input = input("Enter the vector with ',' to separate values: ")
    vector_input = vector_input.split(",")
    return vector_input

# vector1 = input_vector()
# vector2 = input_vector()

def sum_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        print("The vectors must have the same length")
        return
    else:
        vector_sum = []
        for i in range(len(vector1)):
            vector_sum.append(int(vector1[i]) + int(vector2[i]))
        return vector_sum

def diff_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        print("The vectors must have the same length")
        return
    else:
        vector_diff = []
        for i in range(len(vector1)):
            vector_diff.append(int(vector1[i]) - int(vector2[i]))
        return vector_diff

def scalar_product(vector1, vector2):
    if len(vector1) != len(vector2):
        print("The vectors must have the same length")
        return
    else:
        scalar_product = 0
        for i in range(len(vector1)):
            scalar_product += int(vector1[i]) * int(vector2[i])
        return scalar_product

# print("Sum of the vectors:", sum_vectors(vector1, vector2))
# print("Difference of the vectors:", diff_vectors(vector1, vector2))
# print("Scalar product of the vectors:", scalar_product(vector1, vector2))



#####################
# Matrix operations #
#####################

def input_matrix():
    rows = int(input("\nEnter the number of rows: "))
    matrix = []
    for i in range(rows):
        new_row = input(f"Enter the values for row {i+1} with ',' to separate values: ")
        row = new_row.split(",")
        matrix.append(row)
    return matrix

matrix1 = np.array(input_matrix())
matrix2 = np.array(input_matrix())
if matrix1.shape != matrix2.shape:
    print("The matrices must have the same shape")
    quit()

print("Sum of the matrices:", np.add(matrix1, matrix2))
print("Product of the matrices:", np.multiply(matrix1, matrix2))
print("Transpose of the matrix 1:", matrix1.transpose())