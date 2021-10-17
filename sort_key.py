student_tuples = [
        ['john', 'A', 15],
        ['jane', 'B', 12],
        ['dave', 'A', 10],
        ['gans', 'C', 13],
        ['mikly', 'C', 11],
        ['nikc', 'C', 10]
    ]
print(sorted(student_tuples, key=lambda student: (student[1], student[2])))
