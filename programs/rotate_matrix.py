# rotate 90 degrees clockwise a N X N matrix in his place


def rotate(a):
    l = len(a) - 1                      
    for row in range(len(a) // 2):          # only half of the rows because the rotation is all around the matrix 
        for col in range(row, l - row):     #  from row to (l - row)  becuase the npointer is walking to inside the matrix
                                            # the next lines substite the values in for corners and walking clockwise
            temp = a[row][col]      
            a[row][col] = a[l - col][row]
            a[l - col][row] = a[l - row][l - col]
            a[l - row][l - col] = a[col][l - row]
            a[col][l - row] = temp

    for i in range(len(a)):
        print(a[i])

a = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66],
]

rotate(a)
