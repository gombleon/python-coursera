days_year, numbers_parties = list(map(int, input().split()))
weekends = set(range(6, days_year + 1, 7)) | set(range(7, days_year + 1, 7))
strikes = set()
for i in range(numbers_parties):
    a, b = list(map(int, input().split()))
    number = (days_year - a) // b + 1
    strikes |= {a + b * i for i in range(number)}
print(len(strikes - weekends))
