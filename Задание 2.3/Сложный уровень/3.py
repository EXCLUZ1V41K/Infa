k = int(input("Введите число: "))
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
print(days[(k - 1) % 7])
