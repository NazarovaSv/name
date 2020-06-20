# with open('gotu.txt','r') as f:
#     with open('gyt.txt','w') as n:
#         for i in f.readline():
#             result = i.replace('0','{change}').replace('1','0')
#             print(result)
#             result = result.replace('{change}','1')
#             n.write(result)

# data1 = [1,5,8,4,4]
# data2 = [5,8,6,2,4]
# for i, j in enumerate(zip(data1, data2)):
#     print(i,j)

import random
import json
#
#
# def sav(matrix, file):
#     with open(file, 'w') as f:
#         data = {'matrix': matrix}
#         print(type(json.dumps(data)))
#         f.writelines(json.dumps(data))
#
#
# matrix = [[random.randrange(0, 10) for j in range(0, 3)] for i in range(0, 3)]
# sav(matrix, 'matrix.json')
#
# with open('matrix.json', 'r') as f:
#     matrix = json.loads(f.readline())['matrix']
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]%2 == 0:
#             matrix[i][j] = 0
#
# sav(matrix, 'matrix.json')

# import pprint
# with open('sleep.json', 'r', encoding="UTF-8") as f:
#     matrix = json.loads(f.read())
#     print(matrix["Objects"][1]["Address"])
#     pprint.pprint(matrix)
#
# with open('sleep.json', 'w', encoding="UTF-8") as f:
#     sleep = json.load(f)
#     sleep['customer'] = 'CUStomer'
#     f.write(sleep)





# import pprint
# with open('sleep.json', 'r', encoding="UTF-8") as f:
#     sleep = json.loads(f.read())
#     print(sleep)

