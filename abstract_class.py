from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("running")


class Whiteboard:
    def write(self):
        print("its writing")


class Programmer:
    def work(self, com):
        print("Solving problems")
        com.process()


prog1 = Programmer()
prog1.work()
com1 = Laptop()
com1.process()
