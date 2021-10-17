myList1 = list(map(int, input().split()))
myList2 = list(map(int, input().split()))
print(*sorted(list(set(myList1) & set(myList2))))
