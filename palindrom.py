# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
k = int(input())
count = 0
i = 1
while i <= k:
    if 1 <= i < 10:
        count += 1
    elif 10 <= i < 100:
        digit_1 = i % 10
        digit_2 = i // 10
        if digit_1 == digit_2:
            count += 1
    elif 100 <= i < 1000:
        digit_1 = i % 10
        digit_3 = i // 100
        if digit_1 == digit_3:
            count += 1
    elif 1000 <= i < 10000:
        digit_1 = i % 10
        digit_2 = (i // 10) % 10
        digit_3 = (i // 100) % 10
        digit_4 = i // 1000
        if digit_1 == digit_4 and digit_2 == digit_3:
            count += 1
    elif 10000 <= i < 100000:
        digit_1 = i % 10
        digit_2 = (i // 10) % 10
        digit_4 = (i // 1000) % 10
        digit_5 = i // 10000
        if digit_1 == digit_5 and digit_2 == digit_4:
            count += 1
    i += 1
print(count)
