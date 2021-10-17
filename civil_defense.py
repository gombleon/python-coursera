n = int(input())
towns_pos = list(map(int, input().split()))
towns = []
solution = []
for i in range(n):
    point = towns_pos[i], i + 1
    towns.append(point)
    solution.append(0)
towns.sort()
m = int(input())
bomb_shelter_pos = list(map(int, input().split()))
bomb_shelters = []
for i in range(m):
    point = bomb_shelter_pos[i], i + 1
    bomb_shelters.append(point)
bomb_shelters.sort()
i = 0
j = 0
for i in range(n):
    while (j < len(bomb_shelters) - 1 and
           abs(towns[i][0] - bomb_shelters[j][0]) >
           abs(towns[i][0] - bomb_shelters[j + 1][0])):
        j += 1
    a = towns[i][1] - 1
    solution[a] = bomb_shelters[j][1]
print(*solution)
