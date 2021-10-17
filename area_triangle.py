import math
ab = float(input())
bc = float(input())
ac = float(input())
if ab <= bc + ac and bc <= ac + ab and ac <= ab + bc:
    p = (ab + bc + ac) / 2
    area = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    print(area)
