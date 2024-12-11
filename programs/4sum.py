"""
https://leetcode.com/problems/4sum/
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
Note: Solved by using 4 pointer( 2 loops and sliding window )
"""

def four_sum(a: list[int], target: int)-> list[list]:
    a.sort()
    result = []
    for i in range(len(a)-3) :
        for j in range(i +1, len(a) - 2) :
            p1 = j+1
            p2 = len(a) -1
            while p1 < p2 :
                if a[i] + a[j] + a[p1] + a[p2] > target :
                    p2 -= 1
                elif  a[i] + a[j] + a[p1] + a[p2] < target :
                    p1 +=1
                else :
                    partial = [a[i], a[j], a[p1], a[p2]]
                    if partial not in result :
                        result.append(partial)
                    p1 +=1
    return result

a = [-2, -1, 0, 0, 1, 2]
target = 0

print(four_sum(a, target))

