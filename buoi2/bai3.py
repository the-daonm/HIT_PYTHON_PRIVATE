print("Chao mung den CLB Tin Hoc HIT")
print('CLB Tin Hoc HIT truc thuoc khoa CNTT - "10 diem"')

s = "CLB Tin Hoc HIT truc thuoc khoa CNTT"
print(''.join([c for c in s if c.isupper()]))
print(''.join([c for c in s if c.islower()]))

if "CNTT" in s:
  print("Yes")
else:
  print("No")

print(s.swapcase())