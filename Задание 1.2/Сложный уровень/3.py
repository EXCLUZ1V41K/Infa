import math


C = float(input("Введите емкость конденсатора: "))
L = float(input("Введите индуктивность: "))
T = 2 * 3.14 * math.sqrt(L * C)
v = 1 / T
print("Период равен: ", T)
print("Частота равна: ", v)
