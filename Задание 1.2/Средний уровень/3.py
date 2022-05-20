e = float(input("Введите своё число: "))
x = 2.1
p = 1
def scheme(x, p, e):
    a = e ** math.sin(abs(x))
    b = (math.sin(p**2) + x ** 3)
    return (a ** 3) / (b ** 2) 
