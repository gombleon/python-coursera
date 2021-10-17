a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
zero = 10 ** (-9)
det = a * d - b * c
det_x = d * e - b * f
det_y = a * f - c * e
if abs(a) < zero and abs(b) < zero and abs(c) < zero and abs(d) < zero:
    main_rang = 0
    if abs(e) < zero and abs(f) < zero:
        ext_rang = 0
    else:
        ext_rang = 1
elif abs(det) < zero:
    main_rang = 1
    if abs(det_x) < zero and abs(det_y) < zero:
        ext_rang = 1
    else:
        ext_rang = 2
else:
    main_rang = 2
    ext_rang = 2
if abs(main_rang - ext_rang) > zero:
    print(0)
elif abs(main_rang - 2) < zero:
    print(2, det_x / det, det_y / det)
elif abs(main_rang) < zero:
    print(5)
elif abs(main_rang - 1) < zero:
    if abs(b) < zero and abs(d) < zero:
        if abs(a) < zero:
            print(3, f / c)
        else:
            print(3, e / a)
    elif abs(a) < zero and abs(c) < zero:
        if abs(b) < zero:
            print(4, f / d)
        else:
            print(4, e / b)
    elif abs(b) < zero:
        print(1, -c / d, f / d)
    else:
        print(1, -a / b, e / b)
