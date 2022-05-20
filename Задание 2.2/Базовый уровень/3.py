x0 = int(input("Введите кординаты оси A(x0): "))
y0 = int(input("Введите кординаты оси A(y0): "))
x1 = int(input("Введите кординаты оси B(x1): "))
y1 = int(input("Введите кординаты оси B(y1): "))
if x0 and y0 == x1 and y1:
    print("Они равны")
elif x0 and y0 <= x1 and y1:
    print("B, дальше")
elif x0 and y0 >= x1 and y1:
    print("A, дальше")
else:
    print("Введите больше нуля")
