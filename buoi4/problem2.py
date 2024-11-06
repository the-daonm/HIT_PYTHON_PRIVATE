n = int(input())
m = int(input())

a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

c = []
for i in range(max(len(a), len(b))):
    if i < len(a):
        c.append(a[i])
    if i < len(b):
        c.append(b[i])

print(c)
