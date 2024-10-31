def perf(x):
    if x >= 190:
        return "Xuat sac"
    elif x >= 150:
        return "Gioi"
    elif x >= 100:
        return "Kha"
    return "Yeu"


n = int(input())

res = []

for i in range(n):
    name = input()
    p1 = int(input())
    p2 = int(input())
    x = p1 + p2
    s = f"{i + 1} {name} {x} {perf(x)}"
    res.append(s)

for i in res:
    print(i)
