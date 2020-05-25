a = "Hello"
b = "World"
c = '  '
print(a+c+b)

firstname = "Ivan"
lastname = "Ivanov"
age = str(35)
result = f"hello, my name is {firstname}  {lastname} , i am  {age} old"
print(result)
print ("hello, my name is " + firstname + lastname + ", i am " + age + " old")
print(firstname.islower())

list_a = ['a','b','s']
list_a.append('z')
print(list_a)

data1 = [4,5,6]
data1.extend(list_a)
print(data1)

ax = [1,8,5,3]
zx = [9,8,6]
ax.append('z')
zx.append('y')
ax.insert(0,'s')
zx.insert(0,'l')
ax.insert(2,zx)
print(ax)
import pprint
data2 = {'firstname': 'ivan',  'lastname': 'Huk', 'old': age, 'list':[5,8,6,0], 'set':{'k', 'f','s'}, 'dict':{'first':1, 'second':2}}
print(data2)
pprint.pprint(data2)
print('last' in data2)

list_z = [1,5]
result = tuple(list_z)
ret = {'see':'list_z'}
ret1 = {'list_z':'result'}
print(ret)

strac ="wowow"
print(strac[::-1])
if strac[::-1]==strac:
    print("It's palindrome")
else:
    print("It's not palindrome")

data3 = 'sasha 4aaf3, masha 2jbj3'
sasha_age = ' '
masha_age = ' '
counter = 0
change = False
for i in data3:
    for j in i:
       if j.isdigit() and change is False:
        sasha_age +=j
        counter += 1
        if counter >=2:
           change = True
        elif j.isdigit():
            masha_age +=j
print(int(sasha_age) + int(masha_age))

data4 = 'sasha 4aaf3, masha 2jbj3'
age = ''
for i in data4:
        if i.isdigit():
            age+=i
sasha_age = int(age[0:2])
masha_age = int(age[2:4])
name = ''
        if i.isalpha():
            name+=1
print(sasha_age + masha_age)
