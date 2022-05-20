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
