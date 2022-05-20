year = int(input("Введите год: "))
print("Выберите эру")
era = int(input("1 - до нашей эры; 2 - нашей эры: "))
if era <= 2:
    if year % 4 == 0:
        if era == 1:
            print(year, "год до нашей эры - високосный")
        elif era == 2:
            print(year, "год нашей эры - високосный")
    elif era == 1:
        print(year, "год до нашей эры - не високосный")
    else:
        print(year, "год нашей эры - не високосный")
else:
    print("Введены не правильные значения")
