# Polymorphism : Objects have multiple forms
# Duck Typing
# Operator Overloading
# Method Overloading
# Method Overriding

# DUCK TYPING


class PyCharm:

    def execute(self):
        print("compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("My ide is also better")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
