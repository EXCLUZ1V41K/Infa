# Задание 1.1
# Базовый уровень (3)
import math


#n = float(input("Введите число n: "))
#y = float(input("Введите число y: "))
#G = n * (y + 3.5) + math.sqrt(y)
#print("Ответ:", G)

# Cредний уровень (3)

#k = float(input("Введите число k: "))
#y = float(input("Введите число y: "))
#e = float(input("Введите число e: "))
#l = k - y
#if l <= 0:
#    print("Решения нет!")
#else:
#    U = (math.log(l) + y ** 4) / (e ** y + 2.355 * k ** 2)
#    print("Ответ:", U)

# Сложный уровень (3)

#h = float(input("Введите число h: "))
#y = float(input("Введите число y: "))
#A = (math.tan(y ** 3 - h ** 4) + h ** 2) / (math.sin(h) ** 3 + y)
#print("Ответ:", A)

#Задание 1.2
#Базовый уровень (3)

#a = float(input("Введите число a: "))
#b = float(input("Введите число b: "))
#c = a + b
#c1 = a - b
#c2 = a * b
#c3 = a / b
#print("Сумма:", c)
#print("Разность:", c1)
#print("Произведение:", c2)
#print("Частное:", c3)

#Средний уровень(3)

#e = float(input("Введите своё число: "))
#x = 2.1
#p = 1
#def scheme(x, p, e):
#    a = e ** math.sin(abs(x))
#    b = (math.sin(p**2) + x ** 3)
#    return (a ** 3) / (b ** 2)


#print("Ответ:", scheme(x, p, e))

#Сложный уровень(3)

#C = float(input("Введите емкость конденсатора: "))
#L = float(input("Введите индуктивность: "))
#T = 2 * 3.14 * math.sqrt(L * C)
#v = 1 / T
#print("Период равен: ", T)
#print("Частота равна: ", v)


#Задание 2.1
#Базовый уровень (3)

#x = 2
#y = 1
#a = (not(x * y < 0)) and (y > x)
#print(a)

#x = 2
#y = -2
#b = (x >= 2) or (y ** 2 != 5)
#print(b)

#Средний уровень (3)

#n = int(input("n: "))
#m = int(input("m: "))
#k = int(input("k: "))
#l = int(input("l: "))
#print(n + m > k or (n > k and m < l))

#Высокий уровень (3)

#y = float(input("Введите ось Y: "))
#x = float(input("Введите ось X: "))
#if y == 2 and y >= 0 or x >= -1.4 and x <= 1.4:
#    print("Точка падает")
#else:
#    print("Точка не падает")

#Задание 2.2
#Базовый уровень (3)

# x0 = int(input("Введите кординаты оси A(x0): "))
# y0 = int(input("Введите кординаты оси A(y0): "))
# x1 = int(input("Введите кординаты оси B(x1): "))
# y1 = int(input("Введите кординаты оси B(y1): "))
# if x0 and y0 == x1 and y1:
#     print("Они равны")
# elif x0 and y0 <= x1 and y1:
#     print("B, дальше")
# elif x0 and y0 >= x1 and y1:
#     print("A, дальше")
# else:
#     print("Введите больше нуля")

#Средний уровень(3)

# year = int(input("Введите год: "))
# print("Выберите эру")
# era = int(input("1 - до нашей эры; 2 - нашей эры: "))
# if era <= 2:
#     if year % 4 == 0:
#         if era == 1:
#             print(year, "год до нашей эры - високосный")
#         elif era == 2:
#             print(year, "год нашей эры - високосный")
#     elif era == 1:
#         print(year, "год до нашей эры - не високосный")
#     else:
#         print(year, "год нашей эры - не високосный")
# else:
#     print("Введены не правильные значения")

#Сложный уровень(3(a))

# j = int(input("Введите двухзначное число: "))
# if j <= 99:
#     if j % 10 == 3:
#         print("В", j, "числе есть цифра 3")
#     elif j % 10 == 7:
#         print("В", j, "есть цифра 7")
#     else:
#         print("Нету цифры 3 и 7")
# else:
#     print("Введено не правильное число")

#Сложный уровень(3(б))

# j = int(input("Введите двухзначное число: "))
# if j <= 99:
#     if j % 10 == 4:
#         print("В", j, "числе есть цифра 4")
#     elif j % 10 == 8:
#         print("В", j, "есть цифра 8")
#     elif j % 10 == 9:
#         print("В", j, "есть цифра 9")
#     else:
#         print("Нету цифры 4, 8, 9")
# else:
#     print("Введено не правильное число")

#Задание 2.3
#Базовый уровень(3)

# x = 2
# x1 = -0.5
# x2 = 1.5
# y = 1.5
# y1 = 2.3
# y2 = -0.8
# R = float(input("R = "))
# if (x * x + y * y) < R * R:
#     print("Первая точка падает на окр.")
# if (x1 * x1 + y1 * y1) < R * R:
#     print("Вторая точка падает на окр.")
# if (x2 * x2 + y2 * y2) < R * R:
#     print("Третья точка падает на окр.")
# else:
#     print("Точки не падают на окр.")

#Средний уровень(3)

# x = float(input("x = "))
# b = -1.6
# m = 0.9
# n = -1.4
# if abs(b * m) > x * x:
#     y = math.sin(b * m + math.cos(n * x))
#     print("Функция y(x) = ", y)
# elif abs(b * m) < x * x:
#     y = math.cos(b * m - math.sin(x))
#     print("Функция y(x) = ", y)
# elif abs(b * m) == x * x:
#     y = math.sqrt(2.7 ** abs(math.cos(x)) + math.sqrt(abs(b * m * x)))
#     print("Функция y(x) = ", y)
# else:
#     print("Нет решения")

#Сложный уровень(3)

# k = int(input("Введите число: "))
# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# print(days[(k - 1) % 7])

#Задание3.1
#Базовый уровень(3)

# A = float(input("A = "))
# N = float(input("N = "))
# c = A ** N
# print("Ответ:", c)

#Средний уровень(3)

def list_prod(d):
    lst = []
    e = 1
    for i in range(1, d + 3):
        if i == 4 or i == 2:
            lst.append(lst[-1])
            continue
        e *= (i ** 3 - 8) / (i - 4)
        lst.append(e)

    return lst[1:]


def series(x, n):
    s_qr = list_prod(n)
    tmp = -3 / x
    res = 0
    for i in range(1, n + 1):
        tmp *= -27 / x ** 3
        if n == 2:
            continue
        res += tmp * s_qr[i] / (2 * (n - 2))

    return res


print(series(10, 10))

