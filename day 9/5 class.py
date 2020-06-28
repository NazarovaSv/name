class Real1:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

class Real2:
    def __init__(self, name2, age2, city2):
        self.__name = name2
        self.__age = age2
        self.__city = city2

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    @property
    def name2(self):
        return self.__name
    @age.setter
    def name2(self, name):
        self.__name = name

class Real3:
    def __init__(self, name3, age3, city3):
        self.__name = name3
        self.__age = age3
        self.__city = city3

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name


class Real4:
    def __init__(self, name4, age4, city4):
        self.__name = name4
        self.__age = age4
        self.__city = city4

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

class Real5:
    def __init__(self, name5, age5, city5):
        self.__name = name5
        self.__age = age5
        self.__city = city5

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

r1 = Real1('Lecha', 15, 'Minsk')
# print(r1._Real1__name)
print(r1.get_name(), r1.get_city())
r1.set_name('Alex')
r1.set_city('Барановичи')
print(r1.get_name(), r1.get_city())
r1.age = 16
print(r1.age)


r2 = Real2('Sasha', 25, 'Denver')
# print(r2._Real2__age)
print(r2.get_city(), r2.get_age())
r2.set_city('DenverRow')
r2.set_age(26)
print(r2.get_city(), r2.get_age())

r3 = Real3('Hol', 50, 'Oslo')
# print(r3._Real3__city)
print(r3.get_age(),r3.get_name())
r3.set_age(51)
r3.set_name('Holly')
print(r3.get_age(), r3.get_name())


r4 = Real4('Kirill', 5, 'Varshava')
# print(r4._Real4__name)
print(r4.get_name(), r4.get_city())
r4.set_name('Kirillysha')
r4.set_city('Praga')
print(r4.get_name(), r4.get_city())


r5 = Real5('Oly', 27, 'NY')
# print(r5._Real5__city)
print(r5.get_city())
r5.set_city('Brookl')
print(r5.get_city())
