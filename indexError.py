#try except IndexError

a = [1, 2, 3]

try:
    b = a[3]
    print(b)
except IndexError as e:
    print("error message")
    print(e)
