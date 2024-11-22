def e_x(x):
    res = f = 1
    for i in range(1, 101):
        f *= i
        res += x / f
    return res


x = int(input())
print(e_x(x))
