# when find a cell with 0, convert all de column and all de row to 0s


def zero(a):
    # seek a cell with 0 and storage the column in a list and de row in a list
    cols = []
    rows = []
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 0:
                if col not in cols:
                    cols.append(col)
                if row not in rows:
                    rows.append(row)

    # change al columns with 0 using numbers sortage in cols
    for col in cols:
        for row in range(len(a)):
            a[row][col] = 0

    # change al rows with 0 using numbers sortage in rows
    for row in rows:
        for col in range(len(a[0])):
            a[row][col] = 0

    for i in range(len(a)):
        print(a[i])


a = [
    [11, 12, 13, 14, 15, 16, 0],
    [21, 22, 23, 24, 25, 26, 27],
    [31, 32, 33, 0, 35, 36, 37],
    [41, 42, 43, 44, 45, 46, 47],
    [51, 52, 53, 54, 55, 56, 57],
    [61, 62, 63, 65, 65, 66, 67],
]

zero(a)
