def phana(n):
  res = 0
  while n:
    n //= 8
    res += 1
  return res * 3

def phanb(a):
  if isinstance(a, (int, float, complex)):
    return dir(a)
  else:
    return False

a = 1234
print(phana(a))
print(phanb(a))
