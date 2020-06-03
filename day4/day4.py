def result(a, b, c, d):
    """
    sum a and b
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: sum number
    :rtype: int   # сразу подскажит в принте, что если строка или нецелое число напишет ошибку
    """
    if d is False:
        a, b = b, a
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        if b != 0:
            return a / b


print(result(2, 3, '+', True))

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 2]
]
max = 0
for i in A:
    for j in range(len(i)):
        if j == 1 and max < i[j]: # j==1 показывает что в списках берет второй элемент, а не 0
            max = i[j]
print(max)

def max(mat, position):
    position-=1
    if len(mat[0]) >= position:
      max = 0
      for j in mat:
          for i in range(len(j)):
           if i == position and max < j[i]:
             max = j[i]
      return max
    return "Error"
A = [
    [1, 2, 3],
    [15, 5, 12],
    [7, 8, 2]
]
print(max(A,1))

def change(mat, element):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:# i строка j элемент
               mat[i][j]  = 0
    return mat
A = [
    [1, 2, 0],
    [15, 1, 12],
    [0, 8, 1]
]
print(change(A,8))
mat2 = change(A,8)
for i in mat2:
    for j in i:
        print(j, end=' ')

def change(mat):
    a = 0
    b = len(mat[0])-1
    for i in range (len(mat)):
        print(mat[i][0])
        for j in range (len(mat[i])):
            print(mat[i][j])
            if j == a:
               mat[i][j]=1
        if a!=b:
         mat[i][b] = 0

        a+=1
        b-=1
    return mat

A = [
    [8, 2, 4],
    [15, 5, 12],
    [7, 8, 8]
]
print(change(A))

import random
def cange_zero(u, av, max1):
    for i in range(len(u)):
        for j in range(len(u[i])):
            if u [i][j]< av:
                u[i][j] = 0
    return u
def cange_one(u, av, max1):
    for i in range(len(u)):
        for j in range(len(u[i])):
            if u [i][j]> av and u[i][j] !=max1:
                u[i][j] = 0
    return u

def karal(u):
    av = 0
    max1 = 0
    for i in u:
        for j in i:
            av+=j
            if max1 < j:
                max1 = j
    av = int(av/9)
    u = cange_zero(u, av, max1)
    u = cange_one(u, av, max1)
    return u

def change_af(matrix_a,matrix_b):
    pass
def change_bf(matrix_a,matrix_b):
    index = 0
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            if i > index or i == index+1 or i== index+2:
                if i == index+1 and j == index +1:
                    matrix_a[i][j - 1], matrix_b[i][j-1] = matrix_b[i][j-1],matrix_a[i][j - 1]
                    print(matrix_a[i][j-1])
                elif i == index+2 and j == index +2:
                    matrix_a[i][j - 1], matrix_b[i][j - 1] = matrix_b[i][j - 1], matrix_a[i][j - 1]
                    print(matrix_a[i][j-1])
                elif i == index and j == index:
                    print(matrix_a[i][j])
                print(matrix_a[i])


            print(matrix_a[i][j])

n = [
    [8, 2, 4],
    [15, 5, 12],
    [7, 8, 8]
]
print(karal(n))