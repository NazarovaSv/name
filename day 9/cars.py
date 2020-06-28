class Car:
    def __init__(self, brand, model, year, speed):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = speed

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        if 100< speed < 120:
            self._speed = speed
        if 90< speed < 100:
            speed+=5
            print (speed)
        if speed < 90:
            print ('Car return')


d= Car('Toyota', 'Camry', 2019, 120)
print(d.get_speed())
d.set_speed(110)
print(d.get_speed())
d.set_speed(95)
print(d.get_speed())
d.set_speed(60)
print(d.get_speed())
