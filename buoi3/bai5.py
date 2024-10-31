n = int(input())

animals = []
food = []

for i in range(n):
    animals.append(input())
for i in range(n):
    food.append(int(input()))

daily_descriptions = []
for i in range(n):
    daily_descriptions.append((animals[i], food[i]))

total_food = 0
top_eater = ""
lowest_eater_index = 0
mx = -float('inf')
mn = float('inf')

for i in range(n):
    if food[i] >= 5:
        total_food += food[i]
    if food[i] > 100:
        break

for i in range(n):
    if food[i] < mn:
        mn = food[i]
        lowest_eater_index = i
    if food[i] > mx:
        mx = food[i]
        top_eater = animals[i]

print(daily_descriptions)
print(total_food)
print(top_eater)
print(lowest_eater_index)
