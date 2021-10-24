def gauss(mat_a, mat_b):
    column = 0
    while column < len(mat_b):
        max_row = None
        for row in range(column, len(mat_a)):
            if max_row is None or abs(mat_a[row][column]) > abs(mat_a[max_row][column]):
                max_row = row
        if max_row is None:
            return None
        if max_row != column:
            mat_a[max_row], mat_a[column] = mat_a[column], mat_a[max_row]
            mat_b[max_row], mat_b[column] = mat_b[column], mat_b[max_row]
        mat_a[column] = [a / mat_a[column][column] for a in mat_a[column]]
        mat_b[column] /= mat_a[column][column]
        for row in range(column + 1, len(mat_a)):
            mat_a[row] = [(a + k * (-mat_a[row][column])) for a, k in zip(mat_a[row], mat_a[column])]
            mat_b[row] += -mat_b[column] * mat_a[row][column]
        column += 1
    solve_x = [0] * len(mat_b)
    for i in range(len(mat_b) - 1, -1, -1):
        solve_x[i] = (mat_b[i] - sum(x * a for x, a in zip(solve_x[(i + 1):], mat_a[i][(i + 1):])))
    print('OK')
    return solve_x


matrix_a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matrix_b = [1, 1, 1]
print(gauss(matrix_a, matrix_b))
