"""
https://leetcode.com/problems/climbing-stairs/
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*** Note 1: the result is equal to the result of (n-1)  +  result of (n-2)  (because is = to solving n-1 adding 
    a single step an solving n-2 adding a doble step))
    steps(n) = steps(n-1) + steps(n-2)
    Note 2: It could be solved adding resluts un a list to easier access [0,1,2,3,5,8,13...] 

"""

def climb_stairs(n: int)-> int :
    if n == 1 or n == 2 :
        return n
    prev1 = 2
    prev2 = 1
    for _ in range(n -2) :
        curr = prev1 + prev2
        prev1, prev2 = curr, prev1
    return curr

print(climb_stairs(int(input("How high the stairs are? "))))