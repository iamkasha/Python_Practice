class Car:
    # class variables belongs to class namespace. static variables and class variables are same
    wheels = 4

    def __init__(self):
        # Instance variables belongs to instance namespace
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5

print(c1.com, c1.mil, Car.wheels)
print(c2.com, c2.mil, c2.wheels)
