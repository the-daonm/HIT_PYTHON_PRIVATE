k = int(input())
a = [int(input()) for _ in range(k)]

n = int(input())
m = int(input())

if k == n * m:
    mat = [a[i * m:(i + 1) * m] for i in range(n)]
    print(mat)
else:
    print("khong the tao ma tran")