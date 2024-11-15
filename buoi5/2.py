registered = set(input().split())
checked_in = set(input().split())

not_checked_in = registered - checked_in
print(f"Chua check-in: {not_checked_in}")

total_count = len(registered.union(checked_in))
print(f"Tong: {total_count}")

sorted_registered = sorted(registered)
print(sorted_registered)
