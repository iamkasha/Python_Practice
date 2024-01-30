# Parent Class or Super class
class A:

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


# Child class or Sub class. It inherits all the properties of class A i.e Parent class
class B:
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


# Multi-level Inheritance
class C(A, B):
    def feature5(self):
        print("feature 5 working")


a1 = A()

a1.feature1()

b1 = B()

b1.feature1()
b1.feature2()

c1 = C()
c1.feature2()
