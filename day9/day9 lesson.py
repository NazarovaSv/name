# class Person:
#     def __init__(self, name, lastname, surname, age, scor, subject):
#         self.age = age
#         self.name = name
#         self.lastname = lastname
#         self.surname = surname
#         self.scor = []
#         self.person = []
#         self.subject = []
#
#
# class Teacher(Person):
#     pass
#
# class Student(Person):
#
#     def set_teacher(self, teacher):
#         print(teacher.age, teacher.age)
#
#     @property
#     def teacher(self):
#         return self.person
#
#     @teacher.setter
#     def teacher(self, person):
#         print(person.name)
#         print("test")
#         # self.person.append(person)
#
# a = range(10)
# subject = ['math', 'russ', 'paint', 'bilog']
# t = Teacher("Alex", "Alex", "Alex", 30, a, subject)
# s = Student("Petya", "Petya", "Petya", 18, a, subject)
# s.set_teacher(t)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lol= [{1:3},{9:5}]

    def get_lol(self):
        return self.lol

data = []

with open('data.txt', 'r') as f:
    data.append(Person('Alex',12))

with open('student.txt', 'r') as f:
    for i in data:
        i.lol({1:3})


a = Person('Alex', 12)
c = Person('Alex', 8)
n = Person('Alex', 15)

print(a.get_lol())