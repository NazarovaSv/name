from functools import reduce
#
# list = [12, 15, 85, 2, 5, 3]
# print(max(list, key=lambda x: int(x)))

#
# list1 = ['12','15','85','2','5','3']
# print(list(map(lambda x: f'hello {x}', list1)))
#
# dar = [3, 13, 5, 15, 18]
# result = list(map(lambda x: str(x), dar))
# print(result)

# tru = ['Ryu', '1gfilh', 'khgf', 'Kol', '5', '3']
# result = list(filter(lambda x: 'k' in x or 'K' in x, tru))
# print(result)
#
# ret = [12,9,3,9,7]
# result1 = reduce(lambda x,y: x*y if y%3==0 else x, ret)
# print(result1)
#
# ret1 = [1,5,8,3]  #не работает без кратных трем
# result2 = reduce(lambda x,y: x*y, filter(lambda x:  x%3==0, ret1))
# print(result2)

# import  random
# def calculator (func):
#     import time
#
#     def result23():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] время выполения: {} секунд'. format(end - start))
#
#     return result23
#
# def ll(func):
#     def wrapper():
#         func()
#         print('второй декоратор')
#     return wrapper
#
# @ll
# @calculator
# def result():
#     data = [random.randrange(0,2**4) for x in range(0,2 **2)]
#     print(sorted(data))
#
# result()

# def decorat(func):
#     def trus(datas):
#         tros = []
#         for i in datas:
#             if i % 2 == 0:
#                 tros.append(i)
#         func(tros)
#
#     return trus
#
#
# @decorat
# def fred(datas):
#     print(datas)
#
#
# fred([1, 8, 9, 45, 84, 5, 2])


# def decorat(func):
#     def trus(datas):
#         tros = {}
#         for i,j in enumerate(datas,1):
#             tros[j] = 1
#         func(tros)
#     return trus
#
# @decorat
# def fred(datas):
#     print(datas)
#
# fred(["1", "8", "9", "45", "84", "5", "2"])

# def decorat(func):
#      def trus(*args):
#          args = args[::-1]
#          func(*args)
#      return trus
#
# @decorat
# def fred(*args):
#      print(args)
#
# fred(1, 8, 9, 45, 84, 5)

# def decorat(func):
#     def trus(**kwargs):
#         datas = {}
#         for i, j in kwargs.items():
#             datas[str(j)] = str(i)
#
#         func(**datas)
#     return trus
#
# @decorat
# def fred(**kwargs):
#     print(kwargs)
#
# fred(s = 1, d = 8, sq = 9, dq = 45)

# def decorat(func):
#     def trus(*args,**kwargs):
#         datas = {}
#         for i, j in kwargs.items():
#             if j in args:
#                 continue
#             datas[i] = j
#         func(*args,**datas)
#     return trus
#
# @decorat
# def fred(*args, **kwargs):
#     print(args, kwargs)
#
# fred(1,3,4, s = 1, d = 8, sq = 9, dq = 45)
#
# def decorat(func):
#     def trus(details, **kwargs):
#         datas = {}
#         for i, j in kwargs.items():
#              datas[i] = j*details
#         func(details, **datas)
#     return trus
#
# def non(func):
#     def trus(details, **kwargs):
#         print(kwargs)
#         datas = {}
#         for i, j in kwargs.items():
#              datas[i] = 0 if j%3==0 else j
#         func(details, **datas)
#     return trus
#
# @decorat
# @non
# def fred(details, **kwargs):
#     print(kwargs)
#
# fred(details = 15, s = 1, d = 8, sq = 9, dq = 45)

train = [15, 155, 165, 12, 1, 85, 45]
print(list(filter(lambda x: x % 15 == 0, train)))