# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter +=1
#             return 1
#         else:
#             raise StopIteration
# s_iter1 = SimpleIterator(3)
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))

# def simple_genetaror(val):
#     while val>0:
#         val -=1
#         yield 1
#
# gen_inter = simple_genetaror(5)
# print(next(gen_inter))
# print(next(gen_inter))
# print(next(gen_inter))
# print(next(gen_inter))
# print(next(gen_inter))
# print(next(gen_inter))

import re
# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print (result)
# print(result.group(0))
# result = re.findall('^(\w+)', 'AV Analytics Vidhya AV') #напишет перво слово
# result1 = re.findall('^д(\w+)', 'дAV Analytics Vidhya AV')
# result2 = re.findall(r'\b\w\w', 'дAV Analytics Vidhya AV') #когда ищем одно слово r необязательно
# result3 = re.findall(r'\b\w{2}', 'дAV Analytics Vidhya AV')
# result4 = re.findall(r'\b\w{1,2}', 'дAV Analytics Vidhya AV')
# print (result)
# print (result1)
# print (result2)
# print (result3)
# print (result4)

# result5 = re.findall(r'\b\@(\w+\.\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print (result5)
#
# result6 = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# result8 = re.findall(r'\d\w+\-\d\w+\-\d\w+', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print (result8)
# print (result6)
#
# result7 = re.findall(r'\b[AIEOUYaeiouy]\w+', 'AV is largest Analytics community of India')
# print (result7)
#
# result8 = re.findall(r'\b[А-ЯЁ]\w+', 'Таня rety Паша зоря')
# print (result8)

# result9 = re.findall(r'\b[98]\d{9}', '9999999999, 999999-999, 99999x9999')
# print (result9)

result10 = re.findall(r"\b(\w{1,3}\.\d\w{1,3}\.\d\w{1,3}\.\d\w{1,3})", '185.45.98.546, 192.0.2.235, 4546kfvjfkv.njhk.hfhdj, 4546.54.84')
print (result10)

import random
from time import sleep

# def genetaror():
#     while True:
#         sleep(1)
#         yield random.randrange(1,1000)
# gen = genetaror()
# print (next(gen))
# print (next(gen))
import sys
data = 0
for i in sys.argv:
    if i.isdigital():
        data += int(i)

print (data)
