import math


k = float(input("Введите число k: "))
y = float(input("Введите число y: "))
e = float(input("Введите число e: "))
l = k - y
if l <= 0:
   print("Решения нет!")
else:
   U = (math.log(l) + y ** 4) / (e ** y + 2.355 * k ** 2)
   print("Ответ:", U)
