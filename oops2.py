class Computer:

    def __init__(self):
        self.name = 'Uday'
        self.age = 24

    def update(self):
        self.age = 23

    def compare(self, other):
        if self.age == other.age:
            print("they are same")

        else:
            print("they are different")


c1 = Computer()
c2 = Computer()

c1.update()

if c1.compare(c2):
    print('They are same')

print(c1.age)
print(c2.name)
