# Instance Methods => 1. Accessor Methods 2. Mutator Methods
# Class Methods
# Static Methods
"""
    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value
"""


class Student:
    school = 'Cal state'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod  # Decorator for class method
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class in this module")


s1 = Student(34, 67, 92)
s2 = Student(84, 54, 45)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
