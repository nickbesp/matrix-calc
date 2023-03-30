#Создание матрицы
def create():
    print('Введите размеры матрицы через пробел:')
    m, n = map(int, input().split())
    mat = list()
    print(f'Введите строку матрицы длины {n} через пробел {m} раз(а):')
    for i in range(m):
        row = list(map(int, input().split()))
        mat.append(row)
    print('Матрица создана!')
    return mat

#Красивый вывод матрицы
def printMat(matrix):
    for i in matrix:
        print(*i)

#Сложение матриц
def sumMat(mat1, mat2):

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrixes' sizes should be equal!")
    
    result = list()
    for i in range(len(a)):
        row = list()
        for j in range(len(a)):
            row.append(a[i][j] + b[i][j])
        result.append(row)
        
    return result

#Умножение матрицы на число
def multMatNum(matrix, num):
    result = list()
    for i in range(len(matrix)):
        row = list()
        for j in range(len(matrix)):
            row.append(matrix[i][j] * num)
        result.append(row)
    return result

#Произведение матриц
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

#Транспонирование матриц
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

#Определитель матрицы
def det(matrix):

    if len(matrix) != len(matrix[0]):
        raise ValueError('The number of the rows of the matrix should be equal with the number of the columns!')

    if len(matrix) == 2:
        return minor(matrix)
    
    #Правило Лапласа
    summ = 0
    for j in range(len(matrix)):
        elem = matrix[0][j]
        summ += elem * adding(matrix, 0, j)

    return summ

#Алгоритмическое дополнение элемента матрицы
def adding(matrix, i, j):
    if len(matrix) == 2:
        return(minor(matrix) * (-1)**(i + j))

    #Создание матрицы на порядок меньше, для которой будет считаться минор
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

#Минор к элементу матрицы 2x2
def minor(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

print('\n')
print('Что вы хотите сделать? (0 - выйти)')
print('1 - сложение матриц')
print('2 - умножение матрицы на число')
print('3 - произведение матриц')
print('4 - транспортирование матриц')
print('5 - определитель матрицы')
action = int(input())

while action != 0:
    mat1 = create()

    if action == 1:
        mat2 = create()
        print('\n Ответ:')
        printMat(sumMat(mat1, mat2))

    if action == 2:
        print('Введите множитель:')
        num = int(input())
        print('\n Ответ:')
        printMat(multMatNum(mat1, num))

    if action == 3:
        mat2 = create()
        print('\n Ответ:')
        printMat(multMat(mat1, mat2))

    if action == 4:
        print('\n Ответ:')
        printMat(transpos(mat1))

    if action == 5:
        print('\n Ответ:')
        print(det(mat1))

    print('\n')
    print('Что вы хотите сделать? (0 - выйти)')
    print('1 - сложение матриц')
    print('2 - умножение матрицы на число')
    print('3 - произведение матриц')
    print('4 - транспортирование матриц')
    print('5 - определитель матрицы')
    action = int(input())