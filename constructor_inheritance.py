# Parent Class or Super class
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


# Child class or Sub class. It inherits all the properties of class A i.e Parent class
class B:

    def __init__(self):

        print("In B init")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("In C init")

    def feat(self):
        super().feature2()


a1 = C()  # Constructor
a1.feat()
# According MRO (Method Resolution Order) left to right
