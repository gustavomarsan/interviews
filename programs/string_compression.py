# implement a method to perform a basic string compression using the counts of repetead characters
# if the compressed string would not become smaller, the method should return the original string

import os

def stringCompression(a):
    last_char=a[0]
    cont=1
    b=""
    for i in range (len(a)):
        print(last_char)
        new_char=a[i]
        if new_char == last_char :
            cont+=1
        else:
            b+=last_char+str(cont)
            last_char=new_char
            cont=1
    
    b+=last_char+str(cont)
    if len(b) < len(a):
        return b
    else :
        return "No change"


os.system("clear")

print(stringCompression(input()))