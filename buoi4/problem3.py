n = int(input())
m = int(input())
num_list1 = [int(input()) for _ in range(n)]
num_list2 = [int(input()) for _ in range(m)]

list = [x for x in num_list1 if x in num_list2]

print(list)
