"""
https://www.hackerrank.com/challenges/kangaroo/problem

You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction 
(i.e, toward positive infinity).
The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
Example
After one jump, they are both at , (, ), so the answer is YES.
Function Description
Complete the function kangaroo in the editor below.
kangaroo has the following parameter(s):
int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2


"""

def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 != x2:        # if both jumps are equal, they will never meet
        return "NO"
    if v1 < v2:             # set the bigger jump as first kangaroo
        x1, v1, x2, v2 = x2, v2, x1, v1

    while x1 < x2:          # while first kangaroo is behind the second
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
        
    return "NO"
        

x1 = 0
v1 = 3
x2 = 4
v2 = 2  
print(kangaroo(x1, v1, x2, v2))  # Output: YES
