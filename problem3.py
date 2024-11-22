coded_string = input()

s = ""
k = 0
stack = []

for c in coded_string:
    if c.isdigit():
        k = int(c)
    elif c == "[":
        stack.append((s, k))
        s = ""
        k = 0
    elif c == "]":
        ps, n = stack.pop()
        s = ps + s * n
    else:
        s += c

print(s)
