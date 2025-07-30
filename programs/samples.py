"""""
a = "0123456"

print("residuo", len(a) % (2))
for i in range(len(a) // 2):
    print(a[i])

a = "FLAMANTE"
b = sorted(a)
b.sort(reverse=True)
print(a,b)
c = "*".join(b)
print(c)





# conteo sin get
array = [1, 2, 3, 9, 5, 8]
table= {}
for item in array:
    if item in table:
        table[item] +=1
    else:
        table[item] = 1
        
print(table)
for key in table.items() :
    print(key[0], key[1])



string = "10.0.0.0"
a = string.split(".")
print(a)
for n in range(len(a)):
    a[n] = int(a[n])

print(a)


a = "abdabdd"
print(a.count("a"))
print(a[0:3])


 
#my_tuple = (i for i in range(1, 10))  # this does not create a tuple
t = (1, 2, 3, 4, 5, 6)
print(t[0])
print(type(t))


def chess_board_print(a: list[list]) -> None:
    print("------------------------")
    for n in range(len(a)):
        print(a[n])

board = [[0 for _ in range(8)] for _ in range(8)]
    #for m in range(0, 8):
    #    line.append(0)
    
board[5][1] = 1
board[2][7] = 1
chess_board_print(board)    

******
def is_equal(s)-> bool: # check if all the chars are equal
    for x in range(1, len(s)):
        if s[x] != s[0]:
            return False
    return True
    
def is_equal_m(s)-> bool: # check if all the char except the middel are equal
    for x in range(1, len(s)):
        if x == int(len(s)/2):      # if is the char in the center do not validate
            continue
        if s[x] != s[0]:
            return False
    return True
    

def substrCount(n, s):
    a = []
    for i in range(0, n-1):
        for j in range(i+2, n+1):
            if i == j:
                continue
            substr = s[i:j]
            if is_equal(substr):
                a.append(substr)
            if len(substr) % 2 and is_equal_m(substr):
                a.append(substr)
    return len(a)+len(s)
                
s="asasd"
print(substrCount(len(s),s))


from math import sqrt

def commonChild(s1, s2):
    l1 = [x for x in s1]
    l2 = [x for x in s2]
    p = 0   # pointer
    while p < len(l1):
        if l1[p] not in l2:
            l1.pop(p)
            continue
        p +=1
    p = 0
    while p < len(l2):
        if l2[p] not in l1:
            l2.pop(p)
            continue
        p +=1
    print(s1)
    s1 = "".join(l1)
    print(s1)
    print(s2)
    s2 = "".join(l2)
    print(s2)
    c = 0
    substr = []
    for i in range(0, len(s1)-1):
        for j in range(i+1, len(s1)):
            substr.append(s1[i: j+1])
    long = 0  
    for i in range(0, len(s2)-1):
        for j in range(i+1, len(s2)):
            new_sub = s2[i:j+1]
            if new_sub in substr:
                c += 1
                print(new_sub, len(new_sub), i, j+1)
                if len(new_sub) > long:
                    long = len(new_sub)
    print(len(substr))
    print("len 1", len(s1), s1)
    print("len 2", len(s2), s2)
    print("coincidencias", c)
    print(substr)
    return long


#s1 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
#s2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"
#s1 = "HARRY"
#s2 = "SALLY"
#print(commonChild(s1, s2))

s1 = [1, 4, 16, 64]

#print(s1[3:6].index("a"))
#print(s1.count("s"))

number = 16
raiz = sqrt(number)

if raiz in s1:
    print("found")
else:
    print("not foun")

print(s1[0:2].count(raiz))


import random, time

x = [1, 3, 4, 6, 8, 9, 9, 7, 6, 6, 6, 6, 2]
a = "wednesday"
my_set = {letter for letter in a}
b = my_set.copy()
my_set.discard("w")
print("set a = ", my_set)
print("set b = ",b)
c = {1, 5, 3, 6, 8, 9}
c = my_set.union(c)     # concatenate 2 sets
d = {item for item in a}
print(d)
e = set()
#e = {i for i in x}
e = {i for i in x}
print(e)
e.discard(9)
print(e)
print("set c = ", c)
print(random.choice(list(c)))
for val in c:           #iterate a set, unordered
    print(val)

my_list = [letter for letter in a]
print(my_list)
print(my_list)

my_dict = {i:1  for i in my_list}
print(my_dict)
print(my_dict.keys())
my_dict.popitem()
print(my_dict.keys())
my_dict.popitem()
print(my_dict.keys())
my_dict.popitem()
print(my_dict.keys())
my_dict.popitem()
print(my_dict.keys())
print(my_dict)

s = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
for i in range(len(s)//2) :
    print(s[i], s[~i] )


    timeout = 30   # [seconds]

timeout_start = time.time()
print(time.asctime())
while time.time() < timeout_start + timeout:
    test = 0
    if test == 5:
        break
    test -= 1
print(time.asctime())


a = "a"
from math import trunc
print(trunc(6 / -132))
import math, sys
print(6 / -132)
print(sys.version)

2,147,483,648


total_chars_words = 7
maxWidth =  16
paragraph = ["shall", "be"]
print(paragraph)

words = len(paragraph)
spaces = len(paragraph) -1
print("words", words, "spaces", spaces)
free_chars = maxWidth - total_chars_words - spaces
spaces_list = []
for i in range(spaces) :
    spaces_list.append(" ")
i = 0
print(spaces_list)
while free_chars > 0 :
    spaces_list[i%len(spaces_list)] = spaces_list[i%len(spaces_list)]+" "
    i +=1
    free_chars -= 1
new_string = ""
for i in range(len(paragraph) -1) :
    new_string += paragraph[i]
    new_string += spaces_list[i]
new_string += paragraph[-1]
print(new_string)
"""
print("hello"'word'*2)

a = 7
print(a.__str__())

