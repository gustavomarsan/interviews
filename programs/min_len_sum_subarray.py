"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Note: **** sliding window problem ,    GRATER OR EQUAL to the target ****
"""

def minSubArrayLen(target, nums):
    p1 = 0
    p2 = 0
    sum = 0
    min_len = len(nums) +1
    while p2 < len (nums) :
        sum += nums[p2] 
        while sum >= target :
            min_len = min(min_len, (p2 - p1) + 1)
            sum -= nums[p1]
            p1 += 1
        p2 += 1
    return min_len if min_len != len(nums) +1 else 0

nums = [1,1,1,1,1,1]
target = 7
print(minSubArrayLen(target, nums))

            
