try:
    a = int(input("Введіть 1 число "))
    b = int(input("Введіть 2 число "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("На нуль ділити не можна")

#або
d = int(input("Число 1:"))
e = int(input("Число 1:"))

for i in range(10):
    d = d+1
    print(d)
    if d < 10:
        break
    print(d+e) 