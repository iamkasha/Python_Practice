# Inner class in python
class Student:

    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_num)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('KUK', 2)
s2 = Student('nick', 3)

s1.show()
s2.show()

