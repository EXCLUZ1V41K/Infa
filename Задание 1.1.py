# Базовый уровень (3)
import math


n = float(input("Введите число n: "))
y = float(input("Введите число y: "))
G = n * (y + 3.5) + math.sqrt(y)
print("Ответ:", G)

#Cредний уровень (3)

k = float(input("Введите число k: "))
y = float(input("Введите число y: "))
e = float(input("Введите число e: "))
l = k - y
if l <= 0:
   print("Решения нет!")
else:
   U = (math.log(l) + y ** 4) / (e ** y + 2.355 * k ** 2)
   print("Ответ:", U)

#Сложный уровень (3)

h = float(input("Введите число h: "))
y = float(input("Введите число y: "))
A = (math.tan(y ** 3 - h ** 4) + h ** 2) / (math.sin(h) ** 3 + y)
print("Ответ:", A)
