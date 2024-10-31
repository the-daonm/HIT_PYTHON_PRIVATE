def e(x, n):
    res = exp = fac = 1.0
    for i in range(1, n + 1):
        exp *= x
        fac *= i
        res += exp / fac
    return res


def S(n):
    res = fac = 1.0
    for i in range(2, n + 1):
        fac *= i
        res += 1 / fac
    return res


x = float(input())
n = int(input())

print(f"e^{x} = {e(x, 100)}")
print(f"S(n) = {S(n)}")
