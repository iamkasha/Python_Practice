pos = -1

"""
def search(list, number):
    i = 0
    while i < len(list):
        if list[i] == number:
            globals()['pos'] = i
            return True
        i = i + 1
    return False
"""


def search(list, number):
    for e in list:
        if e == number:
            globals()['pos'] = list.index(e)
            return True
    return False


list = [11, 5, 32, 9, 26, 64]
n = int(input("Enter the value of n"))

if search(list, n):
    print("found at", pos)
else:
    print("not found")
 