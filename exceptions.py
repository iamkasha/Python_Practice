a = 5
b = 2

try:
    print("resource open")
    print(a / b)
    k = int(input("Enter a number"))

except ZeroDivisionError as e:
    print("hey, you can't divide a num by Zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong")

finally:
    print("resource closed")

print("Bye!")
