""""
Given a signed integer x, return x with its digits reversed. 32 bit integer [-2^31, 2^31 - 1]

https://leetcode.com/problems/reverse-integer/ 
  
  Tiene edge case en negativos y del tamano del numero (32 bits)  "2,147,483,648"

"""
def reverse_integer(n : int)-> int :
    r = 0
    v = 1
    if n < 0 :
        n = abs(n)
        v = -1
    while abs(n) > 0 :
        mod = n % 10
        n = n // 10
        r = r*10 + mod
    if r > r**31 :
        return 0
    return r*v

print(reverse_integer(123))