list1 = [5, 4, 3, 2, 1]
list2 = []
list3 = []
n =len(list1)
while len(list3) < n:
    if len(list1) > 0 and list1[-1] == 1:
        a = list1.pop()
        list3.append(a)
        print(a, 1, 3)
        if len(list1) > 0 and (len(list2) == 0 or list1[-1] < list2[-1]):
            b = list1.pop()
            list2.append(b)
            print(b, 1, 2)
        elif len(list2) > 0  and (len(list1) == 0 or list2[-1] < list1[-1]):
            b = list2.pop()
            list1.append(b)
            print(b, 2, 1)
    elif len(list3) > 0 and list3[-1] == 1:
        a = list3.pop()
        list2.append(a)
        print(a, 3, 2)
        if len(list3) > 0 and (len(list1) == 0 or list3[-1] < list1[-1]):
            b = list3.pop()
            list1.append(b)
            print(b, 3, 1)
        elif len(list1) > 0 and (len(list3) == 0 or list1[-1] < list3[-1]):
            b = list1.pop()
            list3.append(b)
            print(b, 1, 3)
    elif len(list2) > 0 and list2[-1] == 1:
        a = list2.pop()
        list1.append(a)
        print(a, 2, 1)
        if len(list2) > 0 and (len(list3) == 0 or list2[-1] < list3[-1]):
            b = list2.pop()
            list3.append(b)
            print(b, 2, 3)
        elif len(list3) > 0 and (len(list2) == 0 or list3[-1] < list2[-1]):
            b = list3.pop()
            list2.append(b)
            print(b, 3, 2)
