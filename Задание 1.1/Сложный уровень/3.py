import math


h = float(input("Введите число h: "))
y = float(input("Введите число y: "))
A = (math.tan(y ** 3 - h ** 4) + h ** 2) / (math.sin(h) ** 3 + y)
print("Ответ:", A)
