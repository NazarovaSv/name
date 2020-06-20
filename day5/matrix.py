import random


def mat(b):
    data = []
    data1 = []

    for i in range(0, b):
        strot = []
        strot1 = []

        for j in range(0, b):
            strot.append(random.randrange(0, 50))
            strot1.append(random.randrange(0, 50))

        data.append(strot)
        data1.append(strot1)

    return data, data1


mat(4)
arr1, arr2 = mat(4)


def matrixa(m):
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if i == j:
                m[i][j] = 0
            if i == 0 and j != 0:
                m[i][j] = 1
            if j == 0 and i != 0:
                m[i][j] = 1
            if j == len(m) and i != len(m):
                m[i][j] = 1
            if i == len(m) and j != len(m):
                m[i][j] = 1

    return m


print(matrixa(arr1))
print(matrixa(arr2))


