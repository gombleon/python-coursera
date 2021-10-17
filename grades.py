def countSort(a):
    max_el = max(a) + 1
    cntMarks = [0] * max_el
    for mark in a:
        cntMarks[mark] += 1
    for nowMark in range(max_el):
        print((str(nowMark) + ' ') * cntMarks[nowMark], end='')

marks = list(map(int, input().split()))
countSort(marks)
