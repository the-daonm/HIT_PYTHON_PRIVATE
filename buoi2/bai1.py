a, b = map(int, input().split())

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a // b = {a // b}")
print(f"a ** b = {a ** b}")
print(f"a % b = {a % b}")

if a > b:
  print("a > b")
elif a < b:
  print("a < b")
else:
  print("a = b")

print(f"a and b = {a & b}")
print(f"a or b = {a | b}")
print(f"a xor b = {a ^ b}")
print(f"NOT a == b = {not a == b}")
print(f"a << 5 = {a << 5}")
print(f"a >> 6 = {a >> 6}")

x = bin(a)[2:]
x = x[::-1]
print(f"he 2 dao nguoc cua a la: {x}")