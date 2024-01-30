"""
name space: Area where you create and store object/variable
- Class namespace
- Object/ Instance namespace
"""


class Car:
    # class variables
    wheels = 4

    def __init__(self):
        # instance variables
        self.mil = 10
        self.company = 'bmw'


c1 = Car()
c2 = Car()

c1.mil = 12
Car.wheels = 3

# we can use object name or class name to access class/static variables
print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, Car.wheels)
