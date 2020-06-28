class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age
        self.objects = []

    def set_objects(self, data):
        self.objects.append({'name': data.name})
data= []
with open('teacher.txt','r') as t:
    for i in t.readlines():
        details = i.replace('\n', '').split()
        data.append(Person(details[0], details[1]))

with open('student.txt', 'r') as t:
    for i in t.readlines():
        details = i.replace('\n', '').split()
        for j in data:
            if details[0] == j.name:
                j.set_objects(Person(details[1],details[2]))

for i in data:
    print('__Data__')
    print(i.name, i.age)
    for j in i.objects:
        print(j.name, j.age)