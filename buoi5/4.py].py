import random

N = int(input("Nhap so luong sinh vien (1 <= N <= 100): "))

password_parts = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]

accounts = {}

for i in range(1, N + 1):
    student_id = f"202360{str(i).zfill(4)}"
    random_password = random.choice(password_parts) + student_id
    accounts[f"Account{i}"] = {
        "Username": student_id,
        "Password": random_password
    }

for account, details in accounts.items():
    print(f"{account}: {details}")
