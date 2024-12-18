"""
https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer 
should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""

def sqrt_x(x: int)-> int :
    p1 = 0
    p2 = x
    while p1 <= p2 :
        mid = (p1 + p2) // 2
        if mid * mid > x :
            p2 = mid - 1
        elif mid * mid < x :
            p1 = mid + 1
        else : 
            return mid
    return p2

print(sqrt_x(9))