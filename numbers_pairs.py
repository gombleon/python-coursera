list1 = list(map(int, input().split()))
list2 = list(set(list1))
numbers_pairs = 0
for i in list2:
    n = list1.count(i)
    numbers_pairs += n * (n - 1) // 2
print(numbers_pairs)
