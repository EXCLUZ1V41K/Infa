#Базовый уровень (3)
import math


a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = a + b
c1 = a - b
c2 = a * b
c3 = a / b
print("Сумма:", c)
print("Разность:", c1)
print("Произведение:", c2)
print("Частное:", c3)

#Средний уровень(3)

e = float(input("Введите своё число: "))
x = 2.1
p = 1
def scheme(x, p, e):
    a = e ** math.sin(abs(x))
    b = (math.sin(p**2) + x ** 3)
    return (a ** 3) / (b ** 2)


print("Ответ:", scheme(x, p, e))

#Сложный уровень(3)

C = float(input("Введите емкость конденсатора: "))
L = float(input("Введите индуктивность: "))
T = 2 * 3.14 * math.sqrt(L * C)
v = 1 / T
print("Период равен: ", T)
print("Частота равна: ", v)
