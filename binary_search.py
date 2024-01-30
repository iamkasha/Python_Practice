pos = -1


def binary_search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2  # // gives you integer division

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [4, 7, 8, 12, 45, 99]
n = int(input("enter a number"))

if binary_search(list, n):
    print("Found at", pos)
else:
    print("Not found")
