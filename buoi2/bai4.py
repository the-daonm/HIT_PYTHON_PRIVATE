def inp():
  name = input("nhap ho ten: ")
  age = input("nhap tuoi: ")
  gender = input("nhap gioi tinh: ")
  ms = input("nhap tinh trang hon nhan: ")
  return name, age, gender, ms

def out(name, age, gender, ms):
  print(f"Ho va ten: {name}")
  print(f"Tuoi: {age}")
  print(f"Gioi tinh: {gender}")
  print(f"Tinh trang hon nhan: {ms}")
  print("-" * 30)

def main():
  hit15 = []
  while True:
    name, age, gender, ms = inp()
    hit15.append((name, age, gender, ms))
    con = input("Nhap them? (y/n)").lower()
    if con != 'y':
      break
  
  for person in hit15:
    out(*person)

if __name__ == "__main__":
    main()