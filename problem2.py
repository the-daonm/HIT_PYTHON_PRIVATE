s = input()

cnt = {}

for c in s:
    if c != " ":
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1

print(cnt)

