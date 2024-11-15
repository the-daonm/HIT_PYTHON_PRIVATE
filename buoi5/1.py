A = tuple(map(int, input().split()))
B = tuple(input().split())

avg_A = sum(A) / len(A)
count_greater_avg = sum(1 for x in A if x > avg_A)
print(f"So phan tu lon hon tbc: {count_greater_avg}")

even_A = tuple(x for x in A if x % 2 == 0)
odd_A = tuple(x for x in A if x % 2 != 0)
print(f"Tuple chan: {even_A}")
print(f"Tuple le: {odd_A}")

k = input("Nhap char k:")
count_k_in_B = sum(1 for x in B if x == k)
print(f"So lan '{k}' xuat hien trong B: {count_k_in_B}")

long_strings_B = tuple(x for x in B if len(x) >= 5)
print(f"Do dai lon hon 5 ki tu: {long_strings_B}")

length = min(len(A), len(B))
C = tuple((A[i], B[i]) for i in range(length))
print(f"Tuple C: {C}")
