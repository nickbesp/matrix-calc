#creating a matrix
def create():
    print('Type the size of matrix separated with space:')
    m, n = map(int, input().split())
    mat = list()
    print(f"Type the matrix's row {m} times with length {n} using space:")
    for i in range(m):
        row = list(map(int, input().split()))
        mat.append(row)
    print('The Matrix is created!')
    return mat

#pretty matrix print
def printMat(matrix):
    for i in matrix:
        print(*i)

#the sum of two matrices
def sumMat(mat1, mat2):

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices' sizes should be equal!")
    
    result = list()
    for i in range(len(a)):
        row = list()
        for j in range(len(a)):
            row.append(a[i][j] + b[i][j])
        result.append(row)
        
    return result

#matrix multiplication by a number
def multMatNum(matrix, num):
    result = list()
    for i in range(len(matrix)):
        row = list()
        for j in range(len(matrix)):
            row.append(matrix[i][j] * num)
        result.append(row)
    return result

#multiplication of two matrices
def multMat(m1, m2):
    r = []
    m = []

    if len(m1[0]) != len(m2):
        raise ValueError('The number of columns of first matrix should equate the number of rows of the second matrix!')

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums = 0
            for k in range(len(m2)):
                sums += (m1[i][k] * m2[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m

#transposition of the matrix
def transpos(matrix):
    #Создание пустой матрицы jxi (изначально у нас ixj)
    result = list()
    for i in range(len(matrix[0])):
        row = list()
        for j in range(len(matrix)):
            row.append(0)
        result.append(row)
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

#determinant of the matrix
def det(matrix):

    if len(matrix) != len(matrix[0]):
        raise ValueError('The number of the rows of the matrix should be equal with the number of the columns!')

    if len(matrix) == 2:
        return minor(matrix)
    
    #Laplace's rule (I don't sure the name is correct)
    summ = 0
    for j in range(len(matrix)):
        elem = matrix[0][j]
        summ += elem * adding(matrix, 0, j)

    return summ

#algebraic complement of a matrix element
def adding(matrix, i, j):
    if len(matrix) == 2:
        return(minor(matrix) * (-1)**(i + j))

    #creating a matrix an order of magnitude smaller than the one you pass to the func
    new_mat = list()
    for q in range(len(matrix[0])):
        if q == i:
            continue
        row = list()
        for w in range(len(matrix)):
            if w == j:
                continue
            row.append(matrix[q][w])
        new_mat.append(row)

    return det(new_mat) * (-1)**(i + j)

#a minor or a determinant of a matrix 2x2
def minor(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

print('\n')
print('what do you want to calc? (0 - exit)')
print('1 - the sum of two matrices')
print('2 - matrix multiplication by a number')
print('3 - multiplication of two matrices')
print('4 - transposition of the matrix')
print('5 - determinant of the matrix')
action = int(input())

while action != 0:
    mat1 = create()

    if action == 1:
        mat2 = create()
        print('\n Answer:')
        printMat(sumMat(mat1, mat2))

    if action == 2:
        print('Enter the multiplier:')
        num = int(input())
        print('\n Answer:')
        printMat(multMatNum(mat1, num))

    if action == 3:
        mat2 = create()
        print('\n Answer:')
        printMat(multMat(mat1, mat2))

    if action == 4:
        print('\n Answer:')
        printMat(transpos(mat1))

    if action == 5:
        print('\n Answer:')
        print(det(mat1))

    print('\n')
    print('what do you want to calc? (0 - exit)')
    print('1 - the sum of two matrices')
    print('2 - matrix multiplication by a number')
    print('3 - multiplication of two matrices')
    print('4 - transposition of the matrix')
    print('5 - determinant of the matrix')
    action = int(input())
