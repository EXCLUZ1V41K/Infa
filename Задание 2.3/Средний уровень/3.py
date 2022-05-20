import math


x = float(input("x = "))
b = -1.6
m = 0.9
n = -1.4
if abs(b * m) > x * x:
    y = math.sin(b * m + math.cos(n * x))
    print("Функция y(x) = ", y)
elif abs(b * m) < x * x:
    y = math.cos(b * m - math.sin(x))
    print("Функция y(x) = ", y)
elif abs(b * m) == x * x:
    y = math.sqrt(2.7 ** abs(math.cos(x)) + math.sqrt(abs(b * m * x)))
    print("Функция y(x) = ", y)
else:
    print("Нет решения")
