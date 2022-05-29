n = int(input())
for i in range(1, n + 1):
    if str(i ** 2).endswith(str(i)):
        print(i)
