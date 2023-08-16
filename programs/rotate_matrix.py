# rotate a N X N matrix 

import os

def rotateMatrix(a):
    b=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    for i in range(len(a)):
        for n in range(len(a)):
            #print(i,n)
            b[n][i]=a[i][n]
            print("*",b[n][i])
            print(a[i][n])
            
    return b

os.system("clear")

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]


print((a[0]))
print((a[1]))
print((a[2]))

b=rotateMatrix(a)

print((b[0]))
print((b[1]))
print((b[2]))
