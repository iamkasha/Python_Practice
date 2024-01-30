class Student:
    # Class/static variable
    school = 'ABC'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # accessor method
    def get_m1(self):
        return self.m1

    # mutator method
    def set_m1(self, value):
        self.m1 = value

    @classmethod  # Decorators
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is student class.. in A module")


s1 = Student(34, 67, 82)
s2 = Student(89, 65, 12)

print(s1.avg())
print(Student.getSchool())
Student.info()
