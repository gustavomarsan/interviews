# when find a cell with 0, convert all de column and all de row to 0s


def zero(a):
    # seek a cell with 0 and storage the column in a list and de row in a list
    cols = set()
    rows = set()
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 0:  # add col and row to a set when found a 0
                cols.add(col)
                rows.add(row)
    print(cols, rows)
    # these for walk all the matrix and move to 0 if row or col is in sets
    for row in range(len(a)):
        for col in range(len(a[0])):
            if row in rows or col in cols:
                a[row][col] = 0

    for i in range(len(a)):
        print(a[i])


a = [
    [11, 12, 13, 14, 15, 16, 17],
    [21, 22, 23, 24, 25, 26, 27],
    [31, 32, 33, 0, 35, 36, 37],
    [41, 42, 43, 44, 45, 46, 47],
    [51, 52, 53, 54, 55, 56, 57],
    [61, 62, 63, 0, 65, 66, 67],
]

zero(a)
