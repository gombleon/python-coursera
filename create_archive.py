[free_size, users] = list(map(int, input().split()))
users_data = []
for i in range(users):
    users_data.append(int(input()))
users_data.sort()
max_users_archive = 0
i = 0
while i < len(users_data) and free_size >= users_data[i]:
    free_size -= users_data[i]
    max_users_archive += 1
    i += 1
print(max_users_archive)
